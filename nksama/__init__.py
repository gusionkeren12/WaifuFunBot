from pyrogram import filters , Client
import os 

from nksama.config import API_ID, API_HASH, BOT_TOKEN

bot = Client(
    'bot',
    api_id=os.environ.get('API_ID'),
    api_hash=os.environ['API_HASH'],
    bot_token=os.environ['BOT_TOKEN'],
    plugins=dict(root=f"{__name__}/plugins")
)

help_message = []




    
