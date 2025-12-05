import discord
from discord.ext import commands, tasks
import os
import sys

# ----------------------------------------
# 1. 環境変数からのトークン読み込みとチェック
# ----------------------------------------
# Koyebの環境変数として 'DISCORD_BOT_TOKEN' を設定すること
BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

if not BOT_TOKEN:
    print("🚨 [FATAL ERROR] 環境変数 'DISCORD_BOT_TOKEN' が設定されていません。Koyebの設定を確認してください。")
    # エラーで終了することで、Koyebに問題が環境変数にあることを伝えます。
    sys.exit(1)

# ----------------------------------------
# 2. Botのセットアップ
# ----------------------------------------
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

status_list = [
    "さいつよあらしたいさく",
    "imaですよ",
    "discordさーばーはいってね",
    "きょうのごはんはやきにくww"
]

# ----------------------------------------
# 3. イベントハンドラとタスクの開始
# ----------------------------------------
@bot.event
async def on_ready():
    print(f"✅ ログイン成功: {bot.user} ({bot.user.id})")
    
    # Botが準備完了してからタスクを開始
    if not change_status.is_running():
        change_status.start()

# ----------------------------------------
# 4. 安定したステータス変更タスク
# ----------------------------------------
@tasks.loop(minutes=1)
async def change_status():
    try:
        # current_loop を使ってリストを循環させる
        index = change_status.current_loop % len(status_list)
        current_status = status_list[index]
        
        activity = discord.Game(name=current_status)
        await bot.change_presence(status=discord.Status.online, activity=activity)
        
        print(f"[STATUS CHANGE] ステータス変更完了: {current_status}")

    except Exception as e:
        print(f"❌ [TASK ERROR] change_statusループでエラーが発生しました: {e}")

# ----------------------------------------
# 5. Botの実行
# ----------------------------------------
try:
    bot.run(BOT_TOKEN)
except discord.errors.LoginFailure:
    print("❌ ログイン失敗: トークンが無効です。Koyebの環境変数を確認してください。")
    sys.exit(1)
except Exception as e:
    print(f"❌ 予期せぬ致命的なエラーによりBotが終了しました: {e}")
    sys.exit(1)
