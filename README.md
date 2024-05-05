# vc-notice-bot

VCの入退室を報告するbot

## 使い方

1. 環境変数にサーバーID, 通知用チャンネルID, BOTトークンを設定する
2. `src/vc_notice_bot`に移動
3. `src/vc_notice_bot/main.py` を実行

### 環境変数

- `VC_NOTICE_BOT_TOKEN`: BOTトークン
- `VC_NOTICE_BOT_GUILD_ID`: サーバーID
- `VC_NOTICE_BOT_ALERT_CHANNEL`: 通知を送る先

## 使用ライブラリ

- [discord.py](https://discordpy.readthedocs.io/ja/latest/)