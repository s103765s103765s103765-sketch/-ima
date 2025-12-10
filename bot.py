import discord
from discord.ext import commands, tasks
import itertools # ステータスリストを循環させるためにitertoolsをインポート

# Intentsの設定（必要に応じてカスタムすることも可能です）
intents = discord.Intents.default()
# intents.message_content = True # コマンドなどを使う場合はこれも必要になることがあります

bot = commands.Bot(command_prefix="!", intents=intents)

status_list = [
    "さいつよあらしたいさく",
    "imaですよ",
    "discordさーばーはいってね",
    "きょうのごはんはやきにくww"
]

# itertools.cycleを使用して、リストの要素を順番に取り出し、リストの終端に達したら最初に戻るイテレータを作成
status_iterator = itertools.cycle(status_list)

@bot.event
async def on_ready():
    """ボットがログインし、準備が完了したときに実行されます。"""
    print(f"ログイン: {bot.user}")
    # change_status ループを開始
    if not change_status.is_running():
        change_status.start()

@tasks.loop(minutes=1)
async def change_status():
    """1分ごとに次のステータスに変更します。"""
    # イテレータから次のステータスを取得
    next_status = next(status_iterator)
    
    # discord.Game アクティビティを作成
    activity = discord.Game(name=next_status)
    
    # プレゼンス（ステータス）を変更
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f"ステータスを '{next_status}' に変更しました。")

# ボットを実行（"YOUR_BOT_TOKEN" の部分を実際のトークンに置き換えてください）
# 環境変数などからトークンを読み込むのがセキュリティ上推奨されます
bot.run("YOUR_BOT_TOKEN")
