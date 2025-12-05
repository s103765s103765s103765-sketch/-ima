import discord
from discord.ext import commands, tasks
import itertools # itertoolsを追加
import os          # osモジュールを追加

# 環境変数からトークンを読み込む
# Renderの環境変数として DISCORD_BOT_TOKEN を設定する必要があります
BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

# トークンが設定されていない場合はエラーを出す
if not BOT_TOKEN:
    print("おつかれｗErrer: 環境変数 'DISCORD_BOT_TOKEN' が設定されてないよー")
    exit()

intents = discord.Intents.default()
# intents.message_content = True # コマンドなどを使う場合は必要になることがあります
bot = commands.Bot(command_prefix="!", intents=intents)

status_list = [
    "さいつよあらしたいさく",
    "imaですよ",
    "discordさーばーはいってね",
    "きょうのごはんはやきにくww"
]

# 修正案2（tasks.loopのcurrent_loopを使う方法）を適用
@bot.event
async def on_ready():
    print(f"ログイン: {bot.user}")
    change_status.start()  

@tasks.loop(minutes=1)
async def change_status():
    index = change_status.current_loop % len(status_list)
    current_status = status_list[index]
    
    # Renderでは ActivityType.playing (Game) が一般的です
    activity = discord.Game(name=current_status) 
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f"ステータス変更: {current_status}")

# 実行
bot.run(BOT_TOKEN)
