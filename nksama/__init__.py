from pyrogram import filters , Client
import os , time
from telegraph import Telegraph
StartTime = time.time()

from nksama.config import *


#config vars
API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
bot = Client("nksama", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="{}/plugins".format(__name__)))

x = bot.get_me()

BOT_ID = x.id
BOT_NAME = x.first_name + (x.last_name or "")
BOT_USERNAME = x.username
BOT_MENTION = x.mention
BOT_DC_ID = x.dc_id

print("Bot is Working")

help_message = []

telegraph = Telegraph()
telegraph.create_account(short_name=BOT_USERNAME)


dev_user = [1491497760, 5337900484]

#from nksama config vars
LOG_GROUP_ID = LOG_GROUP_ID
