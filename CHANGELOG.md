# Changelog / 変更履歴

## 1.0.2 — 2026-10-24

- Reserve a unique partial MP4 per job and clean up only files created by that job. Existing partial files and input videos are preserved on success and failure. / ジョブごとに固有の一時MP4を排他的に確保し、自分が作成した一時ファイルだけを削除。成功・失敗とも既存の一時ファイルと入力動画を保持。
- Publish completed output atomically without overwriting concurrent outputs; retry with a numbered filename on collision. Fix dotted-prefix collision loops. / 完成先を上書きせず原子的に確定し、並列処理の衝突時は連番名へ変更。ドットを含む出力名の衝突ループも修正。
- Cover output safety with focused regression tests and Linux/Windows CI. See `VALIDATION.md` for the current real-runtime test scope. / 出力保護の回帰テストとLinux／Windows CIを追加。今回の実処理確認範囲は `VALIDATION.md` を参照。

## 1.0.1 — 2026-09-13

- Display the converted video player and saved path inside the right-hand result node after completion. / 完了後、右側の結果ノード内へ変換後動画プレーヤーと保存先を表示。
- Label the left input preview and right result preview clearly on the workflow canvas. / 左の入力プレビューと右の完成動画プレビューをワークフロー上で明確化。
- Use a timestamp-only workflow filename while keeping the package version in Git tags, Releases, and metadata. / ワークフローファイル名は日時のみとし、配布版はGitタグ・Release・メタデータで管理。
- Validate the preview through both the ComfyUI API and actual browser UI with an H.264/AAC sample. / H.264／AACサンプルを使い、ComfyUI APIと実ブラウザー画面の両方でプレビューを検証。

## 1.0.0 — 2026-09-13

- Initial public release of the sequential, memory-safe long-video upscaler with audio preservation. / 音声を維持する逐次処理型・長尺安全アップスケーラーの初回公開。
