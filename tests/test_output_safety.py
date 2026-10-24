import importlib.util
import io
import os
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import sys
import tempfile
import threading
import types
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]


def load_node():
    stubs = {name: types.ModuleType(name) for name in (
        'cv2', 'numpy', 'torch', 'torch.nn', 'torch.nn.functional',
        'comfy', 'comfy.utils', 'comfy.model_management', 'folder_paths',
    )}
    stubs['torch'].nn = stubs['torch.nn']
    stubs['torch.nn'].functional = stubs['torch.nn.functional']
    stubs['torch'].float16 = 'float16'
    stubs['comfy'].utils = stubs['comfy.utils']
    stubs['comfy'].model_management = stubs['comfy.model_management']
    stubs['comfy.utils'].ProgressBar = lambda total: None
    stubs['comfy.model_management'].get_torch_device = lambda: 'cpu'
    stubs['comfy.model_management'].soft_empty_cache = lambda: None
    cv = stubs['cv2']
    cv.CAP_PROP_FRAME_WIDTH, cv.CAP_PROP_FRAME_HEIGHT = 1, 2
    cv.CAP_PROP_FPS, cv.CAP_PROP_FRAME_COUNT = 3, 4
    with patch.dict(sys.modules, stubs):
        spec = importlib.util.spec_from_file_location('safety_node', ROOT / '__init__.py')
        node = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(node)
    return node


NODE = load_node()


class Video:
    def __init__(self, source):
        self.source = source

    def get_stream_source(self):
        return self.source


class Model:
    def to(self, *args, **kwargs):
        return self

    def cpu(self):
        return self


class Capture:
    def __init__(self, opened=True, frames=1):
        self.opened, self.frames, self.released = opened, frames, False

    def isOpened(self):
        return self.opened

    def get(self, key):
        return {1: 2, 2: 2, 3: 24, 4: self.frames}[key]

    def read(self):
        if self.frames:
            self.frames -= 1
            return True, object()
        return False, None

    def release(self):
        self.released = True


class Output:
    def tobytes(self):
        return b'RGB' * 4


class Process:
    def __init__(self, command, returncode=0):
        self.stdin, self.stderr = io.BytesIO(), io.BytesIO(b'encoder error')
        self.returncode, self.finished = returncode, False
        self.path = Path(command[-1])
        if not self.path.is_file() or self.path.stat().st_size:
            raise AssertionError('temporary output was not exclusively pre-created')
        self.path.write_bytes(b'encoded video')

    def wait(self):
        self.finished = True
        return self.returncode

    def poll(self):
        return self.returncode if self.finished else None

    def kill(self):
        self.finished = True


class OutputSafetyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / 'source.mp4'
        self.source.write_bytes(b'original input')
        self.partial = self.root / 'result.partial.mp4'
        self.partial.write_bytes(b'pre-existing partial')
        self.paths, self.captures = [], []
        self.lock = threading.Lock()
        self.barrier = None
        self.returncode = 0
        self.opened, self.frames = True, 1
        self.launch_error = None
        self.before_publish = None
        self.node = NODE.LongVideoUpscaleSafe()
        self.patches = [
            patch.object(NODE.folder_paths, 'get_output_directory', return_value=str(self.root), create=True),
            patch.object(NODE.cv2, 'VideoCapture', side_effect=self.capture, create=True),
            patch.object(NODE.subprocess, 'Popen', side_effect=self.launch),
            patch.object(self.node, '_upscale_frame', return_value=Output()),
        ]
        for p in self.patches:
            p.start()
            self.addCleanup(p.stop)

    def capture(self, source):
        cap = Capture(self.opened, self.frames)
        self.captures.append(cap)
        return cap

    def launch(self, command, **kwargs):
        with self.lock:
            self.paths.append(Path(command[-1]))
        if self.launch_error:
            raise self.launch_error
        proc = Process(command, self.returncode)
        if self.before_publish:
            self.before_publish()
        if self.barrier:
            self.barrier.wait(timeout=10)
        return proc

    def run_node(self, source=None, prefix='result', model=None):
        return Path(self.node.upscale(Video(self.source if source is None else source),
            Model() if model is None else model, 2, prefix, 'h264', 18, 'fast', 512)['result'][0])

    def assert_preserved(self):
        self.assertEqual(self.source.read_bytes(), b'original input')
        self.assertEqual(self.partial.read_bytes(), b'pre-existing partial')
        self.assertFalse(list(self.root.rglob('.long-video-*.partial.mp4')))
        self.assertTrue(all(cap.released for cap in self.captures))

    def test_success_preserves_existing_partial(self):
        output = self.run_node()
        self.assertEqual(output.read_bytes(), b'encoded video')
        self.assertNotEqual(output, self.paths[0])
        self.assert_preserved()

    def test_failure_preserves_existing_partial(self):
        self.returncode = 1
        with self.assertRaisesRegex(RuntimeError, 'ffmpeg failed'):
            self.run_node()
        self.assertFalse((self.root / 'result.mp4').exists())
        self.assert_preserved()

    def test_input_is_old_partial_path(self):
        output = self.run_node(source=self.partial)
        self.assertEqual(output.read_bytes(), b'encoded video')
        self.assert_preserved()

    def test_input_is_final_path(self):
        output = self.run_node(prefix='source')
        self.assertNotEqual(output, self.source)
        self.assert_preserved()

    def test_input_is_final_path_with_extension(self):
        output = self.run_node(prefix='source.mp4')
        self.assertNotEqual(output, self.source)
        self.assert_preserved()

    def test_dotted_prefix_collision(self):
        existing = self.root / 'result.mp4'
        existing.write_bytes(b'existing result')
        output = self.run_node(prefix='result.partial')
        self.assertEqual(output.name, 'result_00001.mp4')
        self.assertEqual(existing.read_bytes(), b'existing result')
        self.assert_preserved()

    def test_input_alias_is_final_path(self):
        os.link(self.source, self.root / 'result.mp4')
        self.run_node()
        self.assertEqual((self.root / 'result.mp4').read_bytes(), b'original input')
        self.assert_preserved()

    @unittest.skipIf(os.name == 'nt', 'symlink privilege varies on Windows')
    def test_dangling_symlink_preserved(self):
        target = self.root / 'absent.mp4'
        (self.root / 'result.mp4').symlink_to(target)
        self.run_node()
        self.assertTrue((self.root / 'result.mp4').is_symlink())
        self.assertFalse(target.exists())
        self.assert_preserved()

    def test_final_appears_during_encode(self):
        self.before_publish = lambda: (self.root / 'result.mp4').write_bytes(b'other job')
        output = self.run_node()
        self.assertNotEqual(output.name, 'result.mp4')
        self.assertEqual((self.root / 'result.mp4').read_bytes(), b'other job')
        self.assert_preserved()

    def test_parallel_success(self):
        self.barrier = threading.Barrier(4)
        with ThreadPoolExecutor(max_workers=4) as pool:
            outputs = list(pool.map(lambda _: self.run_node(), range(4)))
        self.assertEqual(len(set(outputs)), 4)
        self.assertEqual(len(set(self.paths)), 4)
        self.assertTrue(all(p.read_bytes() == b'encoded video' for p in outputs))
        self.assert_preserved()

    def test_parallel_failure(self):
        self.returncode = 1
        self.barrier = threading.Barrier(4)
        def fail(_):
            with self.assertRaises(RuntimeError):
                self.run_node()
        with ThreadPoolExecutor(max_workers=4) as pool:
            list(pool.map(fail, range(4)))
        self.assertEqual(len(set(self.paths)), 4)
        self.assert_preserved()

    def test_process_launch_failure(self):
        self.launch_error = FileNotFoundError('ffmpeg missing')
        with self.assertRaises(FileNotFoundError):
            self.run_node()
        self.assert_preserved()

    def test_frame_failure(self):
        self.node._upscale_frame.side_effect = RuntimeError('inference failed')
        with self.assertRaisesRegex(RuntimeError, 'inference failed'):
            self.run_node()
        self.assert_preserved()

    def test_broken_encoder_pipe(self):
        class BrokenPipe(io.BytesIO):
            def write(self, data):
                raise BrokenPipeError('encoder exited')
            def close(self):
                super().close()
                raise BrokenPipeError('encoder exited during close')
        original = self.launch
        def launch(command, **kwargs):
            proc = original(command, **kwargs)
            proc.stdin = BrokenPipe()
            return proc
        with patch.object(NODE.subprocess, 'Popen', side_effect=launch):
            with self.assertRaises(BrokenPipeError):
                self.run_node()
        self.assert_preserved()

    def test_zero_frames(self):
        self.frames = 0
        with self.assertRaisesRegex(RuntimeError, 'no decodable frames'):
            self.run_node()
        self.assert_preserved()

    def test_invalid_video(self):
        self.opened = False
        with self.assertRaisesRegex(RuntimeError, 'Could not open video'):
            self.run_node()
        self.assertEqual(self.paths, [])
        self.assert_preserved()

    def test_model_setup_failure(self):
        model = Model()
        model.to = lambda *a, **kw: (_ for _ in ()).throw(RuntimeError('model setup failed'))
        with self.assertRaisesRegex(RuntimeError, 'model setup failed'):
            self.run_node(model=model)
        self.assertEqual(self.paths, [])
        self.assert_preserved()

    def test_publish_failure(self):
        with patch.object(NODE.os, 'link', side_effect=OSError('unsupported filesystem')):
            with self.assertRaisesRegex(OSError, 'unsupported filesystem'):
                self.run_node()
        self.assertFalse((self.root / 'result.mp4').exists())
        self.assert_preserved()

    def test_bytes_source_cleaned_on_validation_failure(self):
        materialize = self.node._materialize_source
        paths = []
        def track(video):
            source, temporary = materialize(video)
            paths.append(Path(temporary))
            return source, temporary
        with patch.object(self.node, '_materialize_source', side_effect=track):
            with self.assertRaisesRegex(ValueError, 'inside'):
                self.run_node(source=io.BytesIO(b'synthetic source'), prefix='../escape')
        self.assertEqual(len(paths), 1)
        self.assertFalse(paths[0].exists())
        self.assert_preserved()


if __name__ == '__main__':
    unittest.main()
