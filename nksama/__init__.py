from pyrogram import Client
import os 
import time

from aiohttp import ClientSession
from pyrogram import Client

StartTime = time.time()
help_message = []


class Log:
    def __init__(self, save_to_file=False, file_name="WaifuFunBot.log"):
        self.save_to_file = save_to_file
        self.file_name = file_name

    def info(self, msg):
        print(f"[+]: {msg}")
        if self.save_to_file:
            with open(self.file_name, "a") as f:
                f.write(f"[INFO]({time.ctime(time.time())}): {msg}\n")

    def error(self, msg):
        print(f"[-]: {msg}")
        if self.save_to_file:
            with open(self.file_name, "a") as f:
                f.write(f"[ERROR]({time.ctime(time.time())}): {msg}\n")


log = Log(True, "bot.log")
aiohttpsession = ClientSession()

from nksama.config import API_ID, API_HASH, BOT_TOKEN

bot = Client(
    'bot',
    api_id=os.environ.get('API_ID'),
    api_hash=os.environ.get('API_HASH'),
    bot_token=os.environ.get('BOT_TOKEN'),
    plugins=dict(root=f"{__name__}/plugins")
)





    
