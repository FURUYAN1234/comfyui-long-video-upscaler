# SNS copy / SNS投稿文

## X short / X短文

```markdown
〖無料配布／ComfyUI〗
長尺動画を1フレームずつ安全に2倍アップスケールするワークフローを公開しました。

✅ 動画全体をRAMへ保持しない逐次処理
✅ 元音声を最後まで維持
✅ 日本語UI
✅ MiniMax H3などの完成MP4へ使用可能

28秒・672フレームを実処理。旧構成約80GB → 最大約2.31GBで完走。

https://github.com/FURUYAN1234/comfyui-long-video-upscaler

#ComfyUI #VideoUpscale #AnimeSharp #生成AI #AI動画
```

## X detailed / X詳細版

```markdown
MiniMax H3などで作った完成動画を、投稿前にもう少し高解像度化したい方向け。

ComfyUI用「長尺動画AnimeSharpアップスケーラー」を無料公開しました。

・1フレームずつ逐次処理
・2倍出力
・H.264／H.265
・CRF、速度、タイルを日本語で変更
・元動画の音声をAACで維持
・失敗時の不完全MP4を削除

実測：864×480 → 1728×960、24fps、28秒、672フレーム。RTX 5080／WSL2で約9分24秒、最大RAM約2.31GB。

モデルはKim2091氏の4x-AnimeSharp（CC BY-NC-SA 4.0）を各自で取得してください。

https://github.com/FURUYAN1234/comfyui-long-video-upscaler

#ComfyUI #MiniMaxH3 #AnimeSharp #動画高画質化 #AI動画
```

## note announcement / note告知

```markdown
ComfyUIで長尺動画をメモリ安全に2倍高解像度化するワークフローを公開しました。

通常の画像バッチ式で約80GBまで膨張してWSLが停止した問題を、1フレームずつ処理する専用ノードで修正。同じ28秒・672フレーム動画を最大約2.31GBで完走し、音声も最後まで維持しました。

導入方法、AnimeSharpの取得先とライセンス、日本語設定、実測結果を記事にまとめています。

GitHub：
https://github.com/FURUYAN1234/comfyui-long-video-upscaler
```
