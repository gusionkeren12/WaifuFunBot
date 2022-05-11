from pyrogram import filters , Client
import os , time
from telegraph import Telegraph
StartTime = time.time()

from nksama.config import API_ID, API_HASH, BOT_TOKEN


#config vars
BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
bot = Client("nksama", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="{}/plugins".format(__name__)))

print("Bot is Working")

help_message = []

telegraph = Telegraph()
telegraph.create_account(short_name=BOT_USERNAME)


dev_user = [1491497760, 5337900484]

LOG_GROUP_ID = "-1001690512977"
