# ComfyUI Long Video AnimeSharp Upscaler / ComfyUI 長尺動画AnimeSharpアップスケーラー

**Source code is public and software use is free. Personal, business, internal and commissioned use, and free integration/provision require no application, prior contact or permission from FURU. Third-party and API terms remain separate. / ソースコード公開・利用無料。個人利用、業務、社内利用、受託制作、無料の組み込み・無料提供には、申請・事前連絡・FURUの許可は不要です。第三者とAPIの条件は別です。**

## Usage terms / 利用条件

> [!NOTE]
> **Current scope / 現行の適用範囲:** Layout 20260913221201 / node v1.0.1: GPL-3.0 for the distributed code/workflow. / 配布コード・ワークフローはGPL-3.0。
>
> Source code is public and software use is free. Personal, business, internal and commissioned use, and free integration/provision require no application, prior contact or permission from FURU. Third-party and API terms remain separate. / ソースコード公開・利用無料。個人利用、業務、社内利用、受託制作、無料の組み込み・無料提供には、申請・事前連絡・FURUの許可は不要です。第三者とAPIの条件は別です。
>
> You may publish, sell, monetize and deliver text, images, comics, videos and other outputs made with the software without application, individual permission, fees or attribution to FURU. / 道具として制作した文章・画像・漫画・動画等は公開・販売・収益化・納品できます。FURUへの申請・個別許可・利用料・クレジット表記は不要です。
>
> Free Web articles, paid note introductions, and independently authored explanations, reviews and courses require no permission, prior contact or fees to FURU if copies or modified versions of the software are not included in the product. / 無料Web記事、note等の有料紹介記事、独自の解説・レビュー・講座は、対象ソフトウェアの複製・改変版を商品に含めなければ、FURUへの許可・事前連絡・利用料は不要です。
>
> FURU permits screenshots and operation videos for introductions insofar as FURU can authorize them, and ordinary links to distribution pages. Check rights and conditions for third-party works, images, materials, audio and other content shown in them separately. / FURUが許諾できる操作画面・操作動画の紹介掲載と、通常の配布ページへのリンクを認めます。掲載した第三者の作品・画像・素材・音声等の権利と条件は別途確認してください。
>
> Free redistribution and integration must follow each applicable license: retain the required copyright/license/third-party notices and identify modifications where required. FURU asks services to make their applicable notices available on an accessible information page, without adding obligations beyond existing licenses. Do not falsely imply official FURU publication, endorsement or partnership. / 無料再配布・無料組み込みでは各適用ライセンスに従い、必要な著作権表示・許諾文・第三者ライセンスを保持し、該当する改変を明示してください。サービスでは利用者が確認できる説明ページに適用条件を案内することをお願いしますが、既存ライセンスを超える義務は追加しません。FURUの公式・公認・提携と偽って表示しないでください。
>
> Current MIT, Apache-2.0 and GPL-3.0 grants also allow software sales, paid distribution, integration into paid offerings, paid functionality and software copies in paid teaching materials or purchaser/member bonuses, subject to the respective license obligations. FURU prior permission is not additionally required for those licensed uses. The seven-app commercialization permission policy is not retroactively imposed on these already licensed projects. A third-party license, model or API may impose separate limits that FURU cannot waive. / 現行のMIT・Apache-2.0・GPL-3.0許諾では、各ライセンスの義務を満たせば、ソフトウェアの販売・有料配布、有料商品等への組み込み、機能の有料提供、有料教材・購入者限定特典・会員向け配布への複製同梱も認められます。その許諾内の利用へFURUの事前許可を追加で求めません。7アプリの商品化の事前許可方針を、既に許諾済みの本プロジェクトへ遡及適用しません。第三者ライセンス・モデル・APIには別の制限があり、FURUは免除できません。
>
> Advertising revenue or voluntary donations alone do not make software access paid in FURU's usage guidance. Internal-only integration, use as your own production tool, commissioned creation and sales/delivery of completed works do not require FURU permission. This does not redefine third-party NonCommercial terms; free access with advertising can still require a separate assessment under those terms. / FURUの利用案内では広告収益や任意の寄付だけでは機能の有料提供として扱いません。社内だけの組み込み、自分で道具として使う受託制作・完成作品の販売・納品にはFURUの許可は不要です。この区分は第三者の非商用条件の意味を変更せず、広告付きの無料提供なども第三者条件を別途判断してください。
>
> If you seek a separately negotiated permission beyond an applicable license, contact FURU with the project/version/files, use, recipients and charging arrangement. Permission is effective when FURU replies by email or another recorded method expressly granting permission and its scope. No paper contract or seal is needed. An inquiry, automatic reply or silence is not permission. The existing licensed uses above require no such inquiry. FURU cannot grant rights belonging to someone else. / 適用ライセンスの範囲外で個別の許可を求める場合は、プロジェクト・版・ファイル、利用方法、提供先、料金の有無を添えてFURUへお問い合わせください。FURUがメール等の記録に残る方法で許可の旨と対象範囲を返信すれば、その範囲で有効です。紙の契約書・押印は不要です。問い合わせ送信、自動返信、無応答だけでは許可になりません。前記の既存許諾内の利用には、この問い合わせは不要です。FURUは他者の権利を許可できません。
>
> Using the software alone does not give FURU rights in your outputs or apply software terms to those outputs. Copies or modified software included in an output remain separately subject to their applicable software licenses. Copyright eligibility/ownership, third-party rights, contracts and API provider terms must be assessed separately. / 利用しただけでFURUが成果物の権利を取得したり、ソフトウェア条件を成果物へ適用したりしません。成果物中のソフトウェア自体の複製・改変部分は、別途その適用ライセンスに従います。著作権の成立・帰属、第三者の権利、契約、API提供元の条件は別途判断してください。
>
> Valid previous MIT, GPL, Apache, Creative Commons and other grants are not revoked or narrowed. Previous releases, existing ZIPs and inherited licensed portions retain their existing permissions. This 2026-10-08 documentation revision clarifies the stated current source commits and designates no new software restrictions. A future change must identify the eligible version, files and rights holder and cannot take away valid earlier grants. / 過去に有効に付与されたMIT・GPL・Apache・Creative Commons等の許諾を取り消したり狭めたりしません。過去版・既存ZIP・従前の許諾を引き継ぐ部分は従来の許諾を保持します。2026-10-08の今回の文書改定は記載した現行ソースコミットの条件を明確化し、新たなソフトウェア制限は指定しません。将来変更する場合は適用可能な版・ファイル・権利者を明示し、以前の有効な許諾を狭めません。
>
> 4x-AnimeSharp is by Kim2091 under CC BY-NC-SA 4.0. FURU cannot waive its noncommercial, attribution, share-alike or change-notice conditions. Paid production requires a separate model-rights assessment. / 4x-AnimeSharpはKim2091のCC BY-NC-SA 4.0モデルです。FURUは非商用・表示・継承・変更表示の条件を免除できません。有料制作ではモデル側の権利を別途判断してください。
>
> [Full guidance / 利用案内全文](FURU_TERMS.md) · [Version, files and rights holders / 版・ファイル・権利者](LICENSE_SCOPE.md) · [Existing LICENSE / 既存LICENSE](LICENSE)


![Workflow overview before conversion / 変換前のワークフロー全体見本](assets/workflow.png)

Node ③ on the right is LongVideoUpscaleSafe: it upscales frames, preserves audio, and saves the MP4. This overview shows the guide on the left and the execution area on the right, with the input selected before running. The result area is empty until a successful run; the converted-video player and save path then appear inside ③. Model-loader node ② is not visible in this screenshot. Before running, select 4x-AnimeSharp.pth in the model loader and check its connection to the upscale-model input of ③. / 右側の「③ 変換後動画をここで再生・保存」が、拡大変換・音声維持・MP4保存を行うLongVideoUpscaleSafeノードです。この画像は左の説明欄と右の実行領域を含む、入力動画を選択した実行前の全体見本です。右下が空欄でも、変換ノードが欠けているわけではありません。実行が正常完了すると、③の下部に変換後動画のプレーヤーと保存先が表示されます。②モデル選択ノードはこの画像では見えていません。実行前にモデル選択ノードで4x-AnimeSharp.pthを選択し、③のアップスケールモデル入力への接続を確認してください。

[Read the release article on note / noteの公開記事を読む](https://note.com/happy_duck780/n/n0f190160e307)

Current layout release: **20260913221201** (custom node v1.0.1) — [GitHub Releases](https://github.com/FURUYAN1234/comfyui-long-video-upscaler/releases/latest)
/ 現行レイアウト配布：**20260913221201**（カスタムノード v1.0.1） — [GitHub Releases](https://github.com/FURUYAN1234/comfyui-long-video-upscaler/releases/latest)

A low-memory ComfyUI workflow and dedicated custom node for upscaling completed videos one frame at a time while keeping the original audio. It is suitable for finished MiniMax H3 videos and other standard video files.
/ 完成済み動画を1フレームずつ低メモリで高解像度化し、元の音声を維持するComfyUIワークフローと専用カスタムノードです。MiniMax H3の完成動画を含む一般的な動画ファイルへ使用できます。

> [!IMPORTANT]
> This is a **post-processing workflow**. Feed it a completed MP4 or another video supported by ComfyUI. It is not inserted into the MiniMax H3 generation graph by default.
> / これは**後処理用ワークフロー**です。MiniMax H3などで完成したMP4を入力します。通常はH3生成ワークフローの途中へ挿入しません。

## Why this workflow exists / このワークフローを作った理由

A conventional video-upscale graph may expand the entire video into one image batch. In the development case, a 28-second, 672-frame input drove the Python process to about 80 GB of resident memory and WSL was terminated by the out-of-memory killer.
/ 一般的な動画アップスケール構成では、動画全体を1つの画像バッチへ展開する場合があります。開発時の28秒・672フレーム入力ではPythonプロセスが約80GBまで増え、WSLがOOMで停止しました。

`LongVideoUpscaleSafe` decodes, upscales, and writes one frame at a time. The same 28-second video completed with a maximum measured ComfyUI RSS of 2,312.4 MiB. This is one measured result on the validation machine, not a guaranteed memory figure for every environment.
/ `LongVideoUpscaleSafe` は、デコード・拡大・書き込みを1フレームずつ行います。同じ28秒動画はComfyUIの最大実測RSS 2,312.4 MiBで完走しました。これは検証PCでの1回の実測であり、すべての環境で同じメモリ量を保証する値ではありません。

## Main benefits / 主な利点

- **Sequential frame processing:** avoids retaining the complete output video as a tensor batch. / **逐次フレーム処理：** 完成動画全体をテンソルバッチとして保持しません。
- **Audio preservation:** maps the source audio into the new MP4 and re-encodes it as AAC. / **音声維持：** 元動画の音声を新しいMP4へ割り当て、AACで再エンコードします。
- **Exact output scale:** choose 1.0x to 4.0x; the included workflow defaults to 2.0x. / **出力倍率指定：** 1.0～4.0倍を指定でき、同梱ワークフローは2.0倍が初期値です。
- **Japanese controls:** scale, file name, codec, CRF, preset, and tile size are labelled in Japanese. / **日本語設定：** 倍率、出力名、コーデック、CRF、速度、タイルサイズを日本語表示します。
- **Guidance on the canvas:** one consolidated English/Japanese guide card explains the run order, processing map, editable settings, installation layout, model license, output, and measured validation. / **キャンバス内ガイド：** 1枚に統合した英日説明欄に、実行順、処理構成図、設定、導入先のファイル構成図、モデルライセンス、保存先、実測結果を記載しています。
- **Result preview in place:** after processing, the finished video player and save location appear in the right-hand result node. / **完成動画をその場で確認：** 処理完了後、右側の結果ノード内に完成動画プレーヤーと保存先を表示します。
- **VRAM fallback:** if full-frame inference runs out of VRAM, tiled inference retries with progressively smaller tiles. / **VRAM不足時の分割処理：** 全画面推論でVRAM不足になった場合はタイルを段階的に縮小して再試行します。
- **Safe output handling:** rejects paths outside `ComfyUI/output`, writes to a partial file, and renames it after success. / **安全な出力処理：** `ComfyUI/output` 外へのパスを拒否し、一時ファイルへ書いた後、成功時に完成名へ変更します。
- **Local processing:** no cloud API, API key, or telemetry is used by this node. / **ローカル処理：** このノードはクラウドAPI、APIキー、テレメトリーを使用しません。

## Included files / 収録内容

```text
comfyui-long-video-upscaler/
├─ __init__.py
├─ workflows/
│  └─ AnimeSharp_LongVideo_Safe_2x_20260913211253.json
├─ assets/
│  ├─ workflow.png
│  └─ note-thumbnail.png
├─ README.md
├─ MODEL_LICENSE.md
├─ VALIDATION.md
├─ CHANGELOG.md
├─ NOTE_ARTICLE.md
├─ SNS_POSTS.md
├─ requirements.txt
├─ pyproject.toml
└─ LICENSE
```

The repository does not include model weights, input videos, generated videos, API keys, personal dictionaries, or development-machine paths.
/ このリポジトリには、モデル本体、入力動画、生成動画、APIキー、個人用辞書、開発PC固有パスを収録していません。

## On-canvas documentation / ワークフロー内の説明欄

The workflow opens with one consolidated bilingual Markdown guide on the left and the three executable nodes on the right, all inside the saved viewport. The left video player is labelled as the input, while the right processing node shows the converted video and save location after completion. It uses ComfyUI's Markdown note, so the guide adds no custom-node dependency.
/ ワークフローは、左に1枚へ統合した英日Markdown説明欄、右に実行する3ノードを置き、すべてが保存済み表示範囲に入る配置です。左の動画プレーヤーは入力、右の処理ノードは完了後の変換済み動画と保存先であることを明記しています。ComfyUIのMarkdown説明欄を使うため、ガイド表示用のカスタムノード依存は増えません。

- Start here and run order. / 最初に読む手順と実行順。
- Per-frame processing and audio flow diagram. / 1フレーム逐次処理と音声結合の構成図。
- Editable settings with starting values. / 変更可能な設定と初期値。
- `ComfyUI/custom_nodes`, `models/upscale_models`, `input`, and `output` file-layout diagram. / 導入先・モデル・入力・出力のファイル構成図。
- Output behavior, license, and measured validation. / 保存動作、ライセンス、実測結果。

## Requirements / 必要環境

- A working [ComfyUI](https://github.com/Comfy-Org/ComfyUI) installation. / 動作する [ComfyUI](https://github.com/Comfy-Org/ComfyUI)。
- NVIDIA CUDA is recommended for practical speed. / 実用的な速度にはNVIDIA CUDAを推奨します。
- `ffmpeg` and `ffprobe` available on `PATH`. / `PATH`から実行できる`ffmpeg`と`ffprobe`。
- Python packages in `requirements.txt`, installed into ComfyUI's actual Python environment. / `requirements.txt`記載のPythonライブラリを、ComfyUIが実際に使うPythonへ導入します。
- `4x-AnimeSharp.pth` in `ComfyUI/models/upscale_models/`. / `ComfyUI/models/upscale_models/`へ配置した`4x-AnimeSharp.pth`。

## Installation / 導入方法

### Option A: ComfyUI Manager Git URL / ComfyUI ManagerのGit URL

Open ComfyUI Manager, choose the Git URL installation function, and enter:
/ ComfyUI ManagerでGit URLからのインストールを選び、次を入力します。

```text
https://github.com/FURUYAN1234/comfyui-long-video-upscaler
```

Restart ComfyUI completely after installation. The workflow embeds the repository identifier so compatible Manager versions can show this repository as the source of the missing custom node.
/ 導入後はComfyUIを完全に再起動してください。ワークフローにはリポジトリ識別情報が入っているため、対応するManagerでは不足カスタムノードの取得元としてこのリポジトリを表示できます。

### Option B: Git clone / Gitで直接導入

Run this inside `ComfyUI/custom_nodes/`.
/ `ComfyUI/custom_nodes/`で次を実行します。

```bash
git clone https://github.com/FURUYAN1234/comfyui-long-video-upscaler.git
```

Install the Python requirements with the interpreter used by ComfyUI.
/ ComfyUIが使用しているPythonへ依存ライブラリを導入します。

```bash
# Linux or WSL venv / Linux・WSLのvenv
/path/to/ComfyUI/.venv/bin/python -m pip install -r "/path/to/ComfyUI/custom_nodes/comfyui-long-video-upscaler/requirements.txt"

# Windows Portable / Windows Portable版
.\python_embeded\python.exe -m pip install -r ".\ComfyUI\custom_nodes\comfyui-long-video-upscaler\requirements.txt"
```

Check FFmpeg before starting ComfyUI.
/ ComfyUI起動前にFFmpegを確認します。

```bash
ffmpeg -version
ffprobe -version
```

## Download the upscale model / アップスケールモデルの取得

The workflow declares the exact model file, directory, and direct download URL in the `UpscaleModelLoader` metadata. Compatible ComfyUI or Manager versions can present it as a missing-model download candidate. If automatic placement is unavailable, download it manually.
/ ワークフローの`UpscaleModelLoader`には、正確なモデル名、配置先、直接ダウンロードURLを登録しています。対応するComfyUIまたはManagerでは、不足モデルの取得候補として表示できます。自動配置できない場合は手動で取得してください。

- File / ファイル：`4x-AnimeSharp.pth`
- Author / 作者：[Kim2091](https://huggingface.co/Kim2091)
- Download / 取得先：[Hugging Face](https://huggingface.co/Kim2091/AnimeSharp/resolve/main/4x-AnimeSharp.pth)
- Model page / モデル説明：[OpenModelDB](https://openmodeldb.info/models/4x-AnimeSharp)
- Destination / 配置先：`ComfyUI/models/upscale_models/4x-AnimeSharp.pth`
- SHA-256 / SHA-256：`e7a7de2dafd7331c1992862bbbcd9e9712a9f9f8e6303f0aaa59b4341d359bab`
- Model license / モデルライセンス：[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

AnimeSharp is not bundled in this repository. Its license requires attribution, non-commercial use, share-alike for adapted material, and indication of changes. Review the model license before use or redistribution.
/ AnimeSharp本体はこのリポジトリへ同梱していません。同モデルのライセンスには表示、非営利、改変物の継承、変更表示の条件があります。利用・再配布前に必ずモデルライセンスを確認してください。

## Load and run the workflow / ワークフローの読み込みと実行

1. Copy `workflows/AnimeSharp_LongVideo_Safe_2x_20260913211253.json` into any ComfyUI workflow folder, or drag it onto the ComfyUI canvas. / JSONを任意のComfyUIワークフローフォルダーへコピーするか、画面へドラッグします。
2. In `ビデオを読み込む`, upload or select the completed source video. / `ビデオを読み込む`で完成済み動画をアップロードまたは選択します。
3. Confirm that `4x-AnimeSharp.pth` is selected. / `4x-AnimeSharp.pth`が選択されていることを確認します。
4. Start with the defaults: 2.0x, H.264, CRF 18, `fast`, tile 512. / 初回は2.0倍、H.264、CRF 18、`fast`、タイル512の初期値で実行します。
5. Click Queue/Run. The finished MP4 is saved under `ComfyUI/output/video/AnimeSharp_2x/`. / 実行すると、完成MP4は`ComfyUI/output/video/AnimeSharp_2x/`へ保存されます。
6. After completion, play the result directly in node ③ on the right. The same node also shows the path below `ComfyUI/output`. / 完了後は右側の③ノード内で変換後動画を再生できます。同じノードに`ComfyUI/output`以下の保存先も表示されます。

## Editable settings / 変更できる設定

| Setting / 設定 | Meaning / 意味 | Recommended first value / 初回推奨 |
|---|---|---|
| `アップスケール倍率` | Output width and height multiplier. / 出力の縦横倍率。 | `2.0` |
| `出力ファイル名` | Relative path below `ComfyUI/output`. / `ComfyUI/output`以下の相対パス。 | `video/AnimeSharp_2x/AnimeSharp_2x` |
| `動画コーデック` | H.264 for compatibility; H.265 for smaller files where supported. / 互換性重視はH.264、対応環境で容量を抑えるならH.265。 | `h264` |
| `画質_CRF` | Lower values increase quality and file size. / 小さいほど高画質・大容量。 | `18` |
| `エンコード速度` | Slower presets improve compression efficiency. / 遅い設定ほど圧縮効率が向上。 | `fast` |
| `タイルサイズ` | VRAM fallback tile; lower it when tiled inference still runs out of memory. / VRAM不足時の分割サイズ。 | `512` |

## What the combined node does / 統合ノードの処理

The graph intentionally has three visible functional nodes: video input, upscale-model loader, and safe long-video processing. The safe node combines video decomposition, frame upscaling, video encoding, audio mapping, and final saving so that a full image batch is never retained.
/ グラフ上の実処理ノードは、動画入力、拡大モデル読み込み、安全な長尺処理の3つです。安全ノードが動画分解、フレーム拡大、動画エンコード、音声割り当て、最終保存を統合し、全画像バッチを保持しない構成にしています。

The player in node ① previews the input video. After a successful run, node ③ displays a separate player for the converted video, reports its path, and keeps the file under `ComfyUI/output/video/AnimeSharp_2x/`.
/ ①ノードのプレーヤーは入力動画の確認用です。正常完了後は③ノード内に変換後動画の別プレーヤーと保存先が表示され、ファイルは`ComfyUI/output/video/AnimeSharp_2x/`へ保存されます。

## Validation / 検証結果

See [VALIDATION.md](VALIDATION.md) for exact measurements and scope. The principal full-length test was 864×480, 24 fps, 28.000 seconds, 672 video frames, and AAC 32 kHz stereo. The result was 1728×960 with the same duration and frame counts. Processing took approximately 563.5 seconds on an RTX 5080 16 GB under WSL2.
/ 詳細は[VALIDATION.md](VALIDATION.md)を参照してください。主な長尺検証は864×480、24fps、28.000秒、672映像フレーム、AAC 32kHzステレオです。出力は1728×960で、時間とフレーム数を維持しました。WSL2・RTX 5080 16GB環境で約563.5秒でした。

## Troubleshooting / トラブル対処

- **Missing custom node:** install this repository under `ComfyUI/custom_nodes` and restart ComfyUI. / **カスタムノード不足：** このリポジトリを`custom_nodes`へ導入しComfyUIを再起動します。
- **Missing model:** place the exact file in `ComfyUI/models/upscale_models/` and refresh models or restart. / **モデル不足：** 正確なファイルを指定先へ置き、モデル一覧更新または再起動を行います。
- **`ffmpeg` not found:** install FFmpeg and add its executable directory to `PATH`. / **FFmpeg不足：** FFmpegを導入し、実行ファイルの場所を`PATH`へ追加します。
- **CUDA out of memory:** try tile 256 or 128; close other GPU applications. / **VRAM不足：** タイル256または128を試し、他のGPUアプリを閉じます。
- **System RAM grows with duration:** confirm that the graph uses `LongVideoUpscaleSafe`, not an image-batch video upscaler. / **動画が長いほどRAMが増え続ける：** 画像バッチ式ではなく`LongVideoUpscaleSafe`を使用しているか確認します。
- **No audio in the result:** first verify that the source file contains an audio stream with `ffprobe`. / **完成動画に音声がない：** `ffprobe`で元動画に音声ストリームがあるか確認します。

## Privacy / プライバシー

The node processes local files and does not transmit media or metadata. The public workflow contains only generic file names and relative output paths.
/ このノードはローカルファイルだけを処理し、動画やメタデータを外部送信しません。公開ワークフローには一般化したファイル名と相対出力先だけを収録しています。

## Licenses / ライセンス

The custom node and workflow in this repository are released under GPL-3.0. See [LICENSE](LICENSE). Third-party model weights are not included and retain their own license. See [MODEL_LICENSE.md](MODEL_LICENSE.md).
/ このリポジトリのカスタムノードとワークフローはGPL-3.0で公開します。[LICENSE](LICENSE)を参照してください。第三者モデルは同梱せず、個別のライセンスが適用されます。[MODEL_LICENSE.md](MODEL_LICENSE.md)を参照してください。

## Credits / クレジット

- [ComfyUI](https://github.com/Comfy-Org/ComfyUI) — GPL-3.0. / ComfyUI本体。
- [AnimeSharp by Kim2091](https://openmodeldb.info/models/4x-AnimeSharp) — CC BY-NC-SA 4.0 model dependency, not bundled. / 使用モデル。CC BY-NC-SA 4.0、非同梱。
- Workflow and custom-node integration by [FURUYAN1234](https://github.com/FURUYAN1234). / ワークフローと専用ノードの統合。
