from pyrogram import filters , Client
import os 
bot = Client(
    'WaifuFunBot',
    api_id=os.environ.get('API_ID'),
    api_hash=os.environ.get('API_HASH'),
    bot_token=os.environ.get('BOT_TOKEN'),
    plugins=dict(root=f"{__name__}/plugins")
)

help_message = []

dev_user = [1491497760]
