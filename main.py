import discord
from discord.ext import commands, tasks
import itertools
import os

# --- 設定部分 ---

# Northflankの環境変数からトークンを読み込みます
# (コードに直接書かないことで、公開リポジトリでも安全になります)
TOKEN = os.getenv("DISCORD_TOKEN")

# ステータスのリスト
status_list = [
    "さいつよあらしたいさく",
    "imaですよ",
    "discordさーばーはいってね",
    "きょうのごはんはやきにくww"
]

# --- ボットの初期化 ---

# メッセージの内容を読み取る権限を有効化 (コマンドを使う場合に必要)
intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix="!", intents=intents)

# リストを無限に循環させるイテレータを作成
status_iterator = itertools.cycle(status_list)

@bot.event
async def on_ready():
    print("--------------------------------------------------")
    print(f"ログイン成功: {bot.user} (ID: {bot.user.id})")
    print("--------------------------------------------------")
    
    # ループが既に回っていない場合のみ開始
    if not change_status.is_running():
        change_status.start()

@tasks.loop(minutes=1)
async def change_status():
    """1分ごとにステータスをリストの次の内容に変更します"""
    try:
        next_status = next(status_iterator)
        await bot.change_presence(activity=discord.Game(name=next_status))
        print(f"[Log] ステータス変更: {next_status}")
    except Exception as e:
        print(f"[Error] ステータス変更中にエラーが発生: {e}")

@bot.event
async def on_connect():
    print("Discordサーバーに接続しました。")

# --- 実行 ---

if __name__ == "__main__":
    if not TOKEN:
        print("【エラー】環境変数 'DISCORD_TOKEN' が設定されていません。")
        print("Northflankの 'Environment Variables' 設定を確認してください。")
    else:
        bot.run(TOKEN)
