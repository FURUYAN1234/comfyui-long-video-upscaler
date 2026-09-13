import io
import os
import subprocess
import tempfile
from pathlib import Path

import cv2
import numpy as np
import torch
import torch.nn.functional as F

import comfy.utils
import folder_paths
from comfy import model_management


class LongVideoUpscaleSafe:
    """Stream video frames through an upscale model without retaining the full video in RAM."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "動画": ("VIDEO",),
                "アップスケールモデル": ("UPSCALE_MODEL",),
                "アップスケール倍率": ("FLOAT", {"default": 2.0, "min": 1.0, "max": 4.0, "step": 0.1, "tooltip": "元動画に対する出力解像度の倍率です。"}),
                "出力ファイル名": ("STRING", {"default": "video/AnimeSharp_2x/AnimeSharp_2x", "tooltip": "ComfyUI/outputからの相対パスです。"}),
                "動画コーデック": (["h264", "h265"], {"default": "h264"}),
                "画質_CRF": ("INT", {"default": 18, "min": 0, "max": 40, "step": 1, "tooltip": "小さいほど高画質でファイルが大きくなります。"}),
                "エンコード速度": (["veryfast", "fast", "medium", "slow"], {"default": "fast", "tooltip": "遅い設定ほど圧縮効率が上がります。"}),
                "タイルサイズ": ("INT", {"default": 512, "min": 128, "max": 1024, "step": 64, "tooltip": "VRAM不足時の分割推論サイズです。通常は512のままで使います。"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("出力ファイルパス",)
    FUNCTION = "upscale"
    CATEGORY = "video/upscale"
    OUTPUT_NODE = True

    @staticmethod
    def _materialize_source(video):
        source = video.get_stream_source()
        if isinstance(source, (str, os.PathLike)):
            return os.fspath(source), None
        if isinstance(source, io.BytesIO):
            source.seek(0)
            tmp = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False)
            tmp.write(source.read())
            tmp.close()
            return tmp.name, tmp.name
        raise TypeError(f"Unsupported video source: {type(source).__name__}")

    @staticmethod
    def _unique_output(prefix, extension):
        output_root = Path(folder_paths.get_output_directory()).resolve()
        clean = prefix.replace("\\", "/").lstrip("/")
        relative = Path(clean)
        if ".." in relative.parts:
            raise ValueError("output_prefix must stay inside the ComfyUI output directory")
        base = output_root / relative
        base.parent.mkdir(parents=True, exist_ok=True)
        candidate = base.with_suffix(extension)
        index = 1
        while candidate.exists():
            candidate = base.with_name(f"{base.name}_{index:05d}").with_suffix(extension)
            index += 1
        return candidate

    @staticmethod
    def _target_size(width, height, factor):
        target_width = max(2, int(round(width * factor)))
        target_height = max(2, int(round(height * factor)))
        target_width += target_width % 2
        target_height += target_height % 2
        return target_width, target_height

    def _upscale_frame(self, frame_bgr, model, device, tile_size, target_width, target_height, pbar):
        rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
        tensor = torch.from_numpy(rgb).permute(2, 0, 1).unsqueeze(0).to(device=device, dtype=torch.float16).div_(255.0)
        try:
            with torch.inference_mode():
                upscaled = model(tensor)
            pbar.update(1)
        except model_management.OOM_EXCEPTION:
            model_management.soft_empty_cache()
            tile = tile_size
            while True:
                try:
                    with torch.inference_mode():
                        upscaled = comfy.utils.tiled_scale(
                            tensor,
                            lambda tile_tensor: model(tile_tensor),
                            tile_x=tile,
                            tile_y=tile,
                            overlap=32,
                            upscale_amount=model.scale,
                        )
                    pbar.update(1)
                    break
                except model_management.OOM_EXCEPTION:
                    tile //= 2
                    if tile < 128:
                        raise
                    model_management.soft_empty_cache()
        if upscaled.shape[-1] != target_width or upscaled.shape[-2] != target_height:
            upscaled = F.interpolate(upscaled, size=(target_height, target_width), mode="bicubic", align_corners=False)
        array = upscaled.squeeze(0).permute(1, 2, 0).clamp_(0, 1).mul_(255).round_().byte().cpu().numpy()
        del tensor, upscaled
        return array

    def upscale(self, 動画, アップスケールモデル, アップスケール倍率, 出力ファイル名, 動画コーデック, 画質_CRF, エンコード速度, タイルサイズ):
        video = 動画
        upscale_model = アップスケールモデル
        upscale_factor = アップスケール倍率
        output_prefix = 出力ファイル名
        codec = 動画コーデック
        crf = 画質_CRF
        preset = エンコード速度
        tile_size = タイルサイズ
        source_path, temporary_source = self._materialize_source(video)
        output_path = self._unique_output(output_prefix, ".mp4")
        partial_path = output_path.with_name(output_path.stem + ".partial" + output_path.suffix)
        cap = cv2.VideoCapture(source_path)
        if not cap.isOpened():
            if temporary_source:
                os.unlink(temporary_source)
            raise RuntimeError(f"Could not open video: {source_path}")

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = float(cap.get(cv2.CAP_PROP_FPS)) or 30.0
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        target_width, target_height = self._target_size(width, height, upscale_factor)
        codec_name = "libx264" if codec == "h264" else "libx265"
        command = [
            "ffmpeg", "-y", "-loglevel", "error",
            "-f", "rawvideo", "-pix_fmt", "rgb24",
            "-s:v", f"{target_width}x{target_height}", "-r", f"{fps:.12g}", "-i", "pipe:0",
            "-i", source_path,
            "-map", "0:v:0", "-map", "1:a?",
            "-c:v", codec_name, "-preset", preset, "-crf", str(crf), "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart",
            str(partial_path),
        ]

        device = model_management.get_torch_device()
        try:
            upscale_model.to(device, dtype=torch.float16)
        except TypeError:
            upscale_model.to(device)
        pbar = comfy.utils.ProgressBar(max(1, frame_count))
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        processed = 0
        error = None
        try:
            while True:
                ok, frame = cap.read()
                if not ok:
                    break
                output = self._upscale_frame(frame, upscale_model, device, tile_size, target_width, target_height, pbar)
                process.stdin.write(output.tobytes())
                processed += 1
                del output
            process.stdin.close()
            stderr = process.stderr.read().decode("utf-8", errors="replace")
            return_code = process.wait()
            if return_code != 0:
                raise RuntimeError(f"ffmpeg failed ({return_code}): {stderr[-4000:]}")
            if processed == 0:
                raise RuntimeError("Input video contained no decodable frames")
            partial_path.replace(output_path)
        except Exception as exc:
            error = exc
            if process.stdin and not process.stdin.closed:
                try:
                    process.stdin.close()
                except Exception:
                    pass
            if process.poll() is None:
                process.kill()
            process.wait()
            if partial_path.exists():
                partial_path.unlink()
        finally:
            cap.release()
            upscale_model.cpu()
            model_management.soft_empty_cache()
            if temporary_source and os.path.exists(temporary_source):
                os.unlink(temporary_source)
        if error:
            raise error
        print(f"LongVideoUpscaleSafe saved {processed} frames to {output_path}")
        return (str(output_path),)


NODE_CLASS_MAPPINGS = {"LongVideoUpscaleSafe": LongVideoUpscaleSafe}
NODE_DISPLAY_NAME_MAPPINGS = {"LongVideoUpscaleSafe": "長尺動画アップスケール（安全・逐次処理）"}
