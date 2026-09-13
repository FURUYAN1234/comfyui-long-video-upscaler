import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WORKFLOW = ROOT / 'workflows' / 'AnimeSharp_LongVideo_Safe_2x_20260913200843.json'
EXPECTED_HASH = 'e7a7de2dafd7331c1992862bbbcd9e9712a9f9f8e6303f0aaa59b4341d359bab'
errors = []

required = [
    '__init__.py', 'README.md', 'MODEL_LICENSE.md', 'VALIDATION.md',
    'NOTE_ARTICLE.md', 'SNS_POSTS.md', 'models.json', 'requirements.txt',
    'pyproject.toml', 'LICENSE', 'assets/workflow.png',
    'assets/note-thumbnail.png', str(WORKFLOW.relative_to(ROOT))
]
for rel in required:
    if not (ROOT / rel).is_file():
        errors.append(f'missing: {rel}')

doc = json.loads(WORKFLOW.read_text(encoding='utf-8'))
node_types = [n.get('type') for n in doc.get('nodes', [])]
for required_type in ['LoadVideo', 'UpscaleModelLoader', 'LongVideoUpscaleSafe', 'MarkdownNote']:
    if required_type not in node_types:
        errors.append(f'missing workflow node: {required_type}')

guides = [n for n in doc.get('nodes', []) if n.get('type') == 'MarkdownNote']
if len(guides) != 1:
    errors.append('workflow must include exactly one visible bilingual guide node')
guide_text = '\n'.join(str(n.get('widgets_values', '')) for n in guides)
for phrase in ['処理構成 / PROCESSING FLOW', 'ファイル配置 / FILE LAYOUT', '変更できる設定 / USER CONTROLS', 'モデルと検証 / MODEL & VALIDATION']:
    if phrase not in guide_text:
        errors.append(f'missing bilingual guide section: {phrase}')
if 'ComfyUI/' not in guide_text or 'custom_nodes/' not in guide_text or 'upscale_models/' not in guide_text:
    errors.append('workflow file-layout diagram is incomplete')
if not doc.get('extra', {}).get('ds'):
    errors.append('workflow has no saved viewport for showing the guide cards')

load = next(n for n in doc['nodes'] if n.get('type') == 'LoadVideo')
if load.get('widgets_values', [None])[0] != 'input_video.mp4':
    errors.append('workflow input filename is not sanitized')
loader = next(n for n in doc['nodes'] if n.get('type') == 'UpscaleModelLoader')
models = loader.get('properties', {}).get('models', [])
if not models or models[0].get('name') != '4x-AnimeSharp.pth':
    errors.append('missing model metadata')
if models and models[0].get('directory') != 'upscale_models':
    errors.append('wrong model directory')

model_doc = json.loads((ROOT / 'models.json').read_text(encoding='utf-8'))['models'][0]
if model_doc.get('sha256') != EXPECTED_HASH or model_doc.get('bundled') is not False:
    errors.append('model manifest mismatch')

for pattern in ['*.pth', '*.pt', '*.safetensors', '*.onnx', '*.mp4', '*.mov', '*.mkv', '*.webm', '*.wav', '*.mp3']:
    for path in ROOT.rglob(pattern):
        errors.append(f'forbidden binary: {path.relative_to(ROOT)}')

secret_patterns = [
    re.compile(r'C:\\Users\\', re.I), re.compile(r'/home/[^/]+/', re.I),
    re.compile(r'AppData', re.I), re.compile(r'sk-[A-Za-z0-9_-]{16,}'),
    re.compile(r'OPENAI_API_KEY\s*[=:]\s*\S+', re.I)
]
for path in ROOT.rglob('*'):
    if '.git' in path.parts or '__pycache__' in path.parts or not path.is_file() or path.suffix.lower() in {'.png', '.jpg', '.jpeg', '.pyc'} or path.name in {'LICENSE', 'verify_public.py'}:
        continue
    try:
        text = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        errors.append(f'unexpected non-UTF-8 file: {path.relative_to(ROOT)}')
        continue
    for pattern in secret_patterns:
        if pattern.search(text):
            errors.append(f'privacy/secret pattern in {path.relative_to(ROOT)}: {pattern.pattern}')

if errors:
    print(json.dumps({'pass': False, 'errors': errors}, ensure_ascii=False, indent=2))
    raise SystemExit(1)
print(json.dumps({'pass': True, 'workflow_nodes': len(doc['nodes']), 'model_sha256': EXPECTED_HASH}, ensure_ascii=False, indent=2))
