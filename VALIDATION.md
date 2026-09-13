# Validation / 検証

## Environment / 環境

- OS / OS構成: WSL2 Ubuntu on Windows
- GPU / GPU: NVIDIA GeForce RTX 5080, 16 GB VRAM
- ComfyUI: 0.35.0
- Frontend / フロントエンド: 1.51.10
- Python: 3.10.6
- PyTorch: 2.13.0+cu130
- Upscale model / 拡大モデル: `4x-AnimeSharp.pth`

## Short test / 短尺検証

A 3.000-second, 864×480, 24 fps, 72-frame video completed in 64.861 seconds and produced 1728×960 output with AAC 32 kHz stereo audio.
/ 3.000秒、864×480、24fps、72フレームの動画を64.861秒で処理し、1728×960、AAC 32kHzステレオの出力を確認しました。

After the result-preview update, a separate 0.500-second, 12-frame H.264/AAC input was run through the installed workflow. It completed in 12.695 seconds and produced a 1728×960, 24 fps, 0.500-second H.264/AAC MP4. The ComfyUI screen showed the input player in node ① and a separate finished-video player in node ③ at the same time. The API history also reported `gifs`, native animated `images`, and `保存先 / Saved to` output metadata.
/ 結果プレビュー更新後、H.264/AAC、0.500秒・12フレームの別入力を導入済みワークフローで実行しました。12.695秒で完了し、1728×960、24fps、0.500秒のH.264/AAC MP4を生成しました。ComfyUI画面では①の入力プレーヤーと③の完成動画プレーヤーが同時に表示されました。API履歴でも`gifs`、標準の動画`images`、`保存先 / Saved to`の出力情報を確認しました。

## Full test / 長尺検証

A 28.000-second, 864×480, 24 fps, 672-frame H.264 input with AAC 32 kHz stereo audio completed in approximately 563.5 seconds. The output was H.264, 1728×960, 24 fps, 28.000 seconds, 672 video frames, and 876 audio frames.
/ 28.000秒、864×480、24fps、672フレーム、H.264映像・AAC 32kHzステレオ音声の入力を約563.5秒で処理しました。出力はH.264、1728×960、24fps、28.000秒、672映像フレーム、876音声フレームでした。

Maximum observed ComfyUI RSS was 2,312.4 MiB. The conventional batch graph that motivated this implementation reached approximately 80 GB RSS and was killed by the OS.
/ ComfyUIの最大実測RSSは2,312.4 MiBでした。本実装のきっかけとなった従来のバッチ構成は約80GBまで増え、OSに停止されました。

Decoded source/output audio correlation was 0.999834. RMS over the final two seconds was 0.160438 for the source and 0.160309 for the output, confirming that decoded audio data remained through the end.
/ デコードした入力・出力音声の相関は0.999834でした。末尾2秒のRMSは入力0.160438、出力0.160309で、音声データが終端まで存在することを確認しました。

Frames at 1.0, 14.0, and 27.5 seconds were visually inspected. No obvious composition or character corruption was observed in those samples.
/ 1.0秒、14.0秒、27.5秒のフレームを目視し、その範囲で明白な構図・人物破綻がないことを確認しました。

## Failure-path checks / 異常系検証

A path containing `../` was rejected before processing, preventing output outside the ComfyUI output directory. Partial MP4 files are removed on processing failure.
/ `../`を含む出力先は処理開始前に拒否され、ComfyUI出力ディレクトリ外への保存を防止しました。処理失敗時には不完全なMP4を削除します。

## Scope / 検証範囲

These are single-run measurements, not averages. Other GPUs, operating systems, codecs, resolutions, frame rates, source formats, and very long durations have not all been tested. Always review the completed video and audio.
/ これらは各条件1回の実測であり平均値ではありません。他GPU、OS、コーデック、解像度、fps、入力形式、さらに長い動画をすべて検証したものではありません。完成動画は必ず映像・音声とも確認してください。
