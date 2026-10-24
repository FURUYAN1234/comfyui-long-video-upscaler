"""Build deterministic tracked-source ZIPs or verify an extracted release."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import zipfile

MANIFEST = 'SHA256SUMS.json'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def verify(root):
    expected = json.loads((root / MANIFEST).read_text(encoding='utf-8'))
    actual = {p.relative_to(root).as_posix(): sha(p.read_bytes())
              for p in root.rglob('*') if p.is_file() and p.relative_to(root).as_posix() != MANIFEST}
    if expected != actual:
        missing = sorted(expected.keys() - actual.keys())
        extra = sorted(actual.keys() - expected.keys())
        changed = sorted(k for k in expected.keys() & actual.keys() if expected[k] != actual[k])
        raise SystemExit(f'Package mismatch: missing={missing}, extra={extra}, changed={changed}')
    print(json.dumps({'pass': True, 'files': len(actual)}, sort_keys=True))


def build(destination):
    root = Path(__file__).resolve().parent
    names = subprocess.check_output(['git', 'ls-files', '-z'], cwd=root).decode().split('\0')
    files = {name: (root / name).read_bytes() for name in names if name}
    files[MANIFEST] = (json.dumps({k: sha(v) for k, v in sorted(files.items())},
                                sort_keys=True, indent=2) + '\n').encode()
    with zipfile.ZipFile(destination, 'x', compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 10, 24, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    print(json.dumps({'zip': str(destination), 'sha256': sha(destination.read_bytes())}, sort_keys=True))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path, nargs='?')
    parser.add_argument('--build', type=Path)
    args = parser.parse_args()
    if args.build:
        build(args.build)
    elif args.root:
        verify(args.root)
    else:
        parser.error('provide an extracted root or --build ZIP')
