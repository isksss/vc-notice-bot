import discord
import config

class Bot():
    """
    Botアプリケーションクラス
    """

    def __init__(self) -> None:
        """
        各種設定値を取得しクラス変数へ格納
        """
        cfg = config.Config()
        self.guild_id = int(cfg.getGuildId())
        self.alert_channel = int(cfg.getNoticeChannel())
        self.bot_token = cfg.getToken()

    def run(self):
        """
        メイン
        クライアントを作成, 各種イベントを設定する.
        todo: クライアント取得, ギルド取得, などを関数へ切り出す 
        todo: VC間移動を通知へ出す? 要検討
        """

        #  clientを取得
        intents = discord.Intents.default()
        intents.message_content = True
        client = discord.Client(intents=intents)

        # 鯖を取得
        guild = client.get_guild(self.guild_id)

        # 通知用チャンネル
        channel = guild.get_channel(self.alert_channel)

        # ===== イベントを設定する =====
        @client.event
        async def on_ready():
            """
            botの準備が完了した際, コンソールにログを出力
            """
            print(f'We have logged in as {client.user}')
        
        @client.event
        async def on_voice_state_update(member, before, after):
            """
            VCチャンネルに入退室した際に指定したチャンネルへ通知を送信する
            """

            # VC入退室が発生した時にメッセージを送信する
            # VC間の移動は通知しない
            if before.channel != after.channel:

                # 入室したとき
                if before.channel is None:
                    msg = f'{member.nick}({member.name}) が {after.channel.name} に参加しました。'
                    await channel.send(msg)

                # 退室したとき
                elif after.channel is None:
                    msg = f'{member.nick}({member.name}) が {before.channel.name} から退出しました。'
                    await channel.send(msg)

        # ===== イベントの設定ここまで =====

        # BOTを実行する
        client.run(self.bot_token)