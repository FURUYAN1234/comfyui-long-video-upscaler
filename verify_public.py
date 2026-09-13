import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WORKFLOW = ROOT / 'workflows' / 'AnimeSharp_LongVideo_Safe_2x_20260913211253.json'
EXPECTED_HASH = 'e7a7de2dafd7331c1992862bbbcd9e9712a9f9f8e6303f0aaa59b4341d359bab'
EXPECTED_VERSION = '1.0.1'
errors = []

required = [
    '__init__.py', 'README.md', 'MODEL_LICENSE.md', 'VALIDATION.md', 'CHANGELOG.md',
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
if '入力は左・完成動画は右 / INPUT LEFT・RESULT RIGHT' not in guide_text:
    errors.append('workflow does not clearly distinguish input and result locations')
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
result_node = next(n for n in doc['nodes'] if n.get('type') == 'LongVideoUpscaleSafe')
if result_node.get('properties', {}).get('ver') != EXPECTED_VERSION:
    errors.append('workflow custom-node version does not match release version')
if '変換後動画をここで再生・保存' not in result_node.get('title', ''):
    errors.append('result node title does not explain preview and save behavior')
if result_node.get('size', [0, 0])[1] < 500:
    errors.append('result node is too small for the embedded video player')

model_doc = json.loads((ROOT / 'models.json').read_text(encoding='utf-8'))['models'][0]
if model_doc.get('sha256') != EXPECTED_HASH or model_doc.get('bundled') is not False:
    errors.append('model manifest mismatch')

pyproject_text = (ROOT / 'pyproject.toml').read_text(encoding='utf-8')
version_match = re.search(r'^version\s*=\s*"([^"]+)"', pyproject_text, re.MULTILINE)
if not version_match or version_match.group(1) != EXPECTED_VERSION:
    errors.append('pyproject version does not match release version')

node_source = (ROOT / '__init__.py').read_text(encoding='utf-8')
for token in ['"gifs": [preview]', '"images": [{', '"animated": (True,)', '保存先 / Saved to:']:
    if token not in node_source:
        errors.append(f'missing result-preview implementation: {token}')

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
