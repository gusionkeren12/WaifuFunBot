from pyrogram import filters , Client
import os 

from nksama.config import API_ID, API_HASH, BOT_TOKEN

class Log:
    def __init__(self, save_to_file=False, file_name="nanamori.log"):
        self.save_to_file = save_to_file
        self.file_name = file_name

bot = Client(
    'bot',
    api_id=os.environ.get('API_ID'),
    api_hash=os.environ.get('API_HASH'),
    bot_token=os.environ.get('BOT_TOKEN'),
    plugins=dict(root=f"{__name__}/plugins")
)

help_message = []

dev_user = [1491497760,5145883564, 5175767264]
