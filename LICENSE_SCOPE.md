# License scope and existing permissions / ライセンス適用範囲と既存の許諾

Documentation revision / 文書改定: 2026-10-08. Software baseline / ソフトウェア基準: **Layout 20260913221201 / node v1.0.1**, commit `ed4bcb376ee67558b15d834e624b262b33622de2`.

This document clarifies rights; it does not replace [LICENSE](LICENSE), impose additional restrictions on existing software, change version numbers or republish ZIPs. / 本書は権利の説明です。[LICENSE](LICENSE)を置き換えず、既存ソフトウェアへ独自制限を加えず、版番号変更やZIP再公開も行いません。

| Scope / 対象 | Rights and applicable terms / 権利と適用条件 |
|---|---|
| Current code and workflow / 現行コード・ワークフロー | GPL-3.0 for the distributed code/workflow. / 配布コード・ワークフローはGPL-3.0。 |
| Rights holders / 権利者 | FURU/FURUYAN1234 workflow and node contributions; ComfyUI contributors and Kim2091 (AnimeSharp model) retain their rights. / ワークフロー・ノードのFURU/FURUYAN1234寄与部分、ComfyUI寄与者、Kim2091（AnimeSharpモデル）はそれぞれの権利を保持。 |
| Third-party models and services / 第三者モデル・サービス | 4x-AnimeSharp is by Kim2091 under CC BY-NC-SA 4.0. FURU cannot waive its noncommercial, attribution, share-alike or change-notice conditions. Paid production requires a separate model-rights assessment. / 4x-AnimeSharpはKim2091のCC BY-NC-SA 4.0モデルです。FURUは非商用・表示・継承・変更表示の条件を免除できません。有料制作ではモデル側の権利を別途判断してください。 |
| Existing releases and ZIPs / 既存Release・ZIP | Keep the license shipped with the acquired version; no retrospective custom restrictions. / 取得した版に付属する許諾を保持し、独自制限は遡及適用しません。 |
| Custom terms target in this revision / 今回の独自条件適用対象 | None of the existing code, workflow JSONs or inherited licensed files. / 既存コード・ワークフローJSON・従前許諾のあるファイルには新規適用しません。 |

Existing MIT/GPL/Apache grants allow paid distribution and commercial use subject to their respective obligations. No additional FURU application, permission or fee is required for those licensed uses. This does not authorize a noncommercial third-party model for commercial use. / 既存のMIT・GPL・Apache許諾は、それぞれの義務を守る有料配布・商用利用を認めます。その許諾内の利用についてFURUへの追加申請・許可・利用料は不要です。第三者の非商用モデルの商用利用まで許可するものではありません。

Retain the license texts and copyright/NOTICE files that apply to each component. Modified redistribution must satisfy the respective license, including source and notice obligations where applicable. The request to display service notices does not add a new requirement to MIT/GPL/Apache-only services. / 各構成要素のライセンス本文・著作権表示・NOTICEを保持してください。改変再配布では各許諾に従い、該当する対応ソースや表示の義務を満たしてください。サービス説明ページへの表示のお願いを、MIT・GPL・Apacheだけのサービスへ追加するものではありません。

See [component/model notices](MODEL_LICENSE.md) and [FURU usage guidance](FURU_TERMS.md). / [構成要素・モデルの条件](MODEL_LICENSE.md)と[FURUの利用案内](FURU_TERMS.md)を参照してください。

## File-level scope / ファイルごとの範囲

| Files/components / ファイル・構成要素 | Rights and conditions / 権利・条件 |
|---|---|
| `__init__.py`, `workflows/AnimeSharp_LongVideo_Safe_2x_20260913211253.json`, root scripts/documents / ルート処理・文書 | GPL-3.0; FURU additions do not remove inherited copyleft / FURU追加部分でも継承元のGPL義務を除外しません |
| Separately downloaded `4x-AnimeSharp.pth` / 別途取得モデル | Kim2091, CC BY-NC-SA 4.0 |

Use per-file headers, bundled LICENSE/NOTICE files and the pinned source commit to resolve individual third-party contributions; the repository owner is not asserted to own all bundled material. / 個々の第三者寄与はファイル内表示・同梱LICENSE/NOTICE・上記ソースコミットで確認し、リポジトリ所有者が同梱物すべての権利者であるとは扱いません。
