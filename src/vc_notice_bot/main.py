import bot


def main():
    """
    エントリポイント
    BOTクライアントを作成して実行
    """
    app = bot.Bot()
    app.run()


if __name__ == "__main__":
    main()
