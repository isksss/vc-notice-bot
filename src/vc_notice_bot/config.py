import os


class Config:
    """
    設定を取得するクラス
    todo: トークンが存在しないときの処理
    """

    def __init__(self) -> None:
        pass

    def getToken(self) -> str:
        """
        環境変数からdiscordTokenを取得する
        ない場合は空文字を返す
        """

        token = os.environ.get("VC_NOTICE_BOT_TOKEN", "")
        return token

    def getNoticeChannel(self) -> str:
        """
        通知を送るチャンネルIDを環境変数から取得
        """
        token = os.environ.get("VC_NOTICE_BOT_ALERT_CHANNEL", "")
        return token

    def getGuildId(self) -> str:
        """
        監視対象のサーバーIDを環境変数から取得
        """
        token = os.environ.get("VC_NOTICE_BOT_GUILD_ID", "")
        return token
