from pyrogram import filters , Client
import os 

bot = Client(
    'bot',
    api_id=os.environ.get('API_ID'),
    api_hash=os.environ['API_HASH'],
    bot_token=os.environ['BOT_TOKEN'],
    plugins=dict(root=f"{__name__}/plugins")
)

help_message = []



SUPPORT_CHAT = os.environ.get('SUPPORT_CHAT', None)
UPDATES_CHANNEL = os.environ.get('UPDATES_CHANNEL', None)

 from nksama.config import Config
 SUPPORT_CHAT = Config.SUPPORT_CHAT
 UPDATES_CHANNEL = Config. UPDATES_CHANNEL
