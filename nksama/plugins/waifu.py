import requests

from nksama import bot 
from pyrogram import filters


bot.on. message(filters.command('waifu'))
def waifu(_,message):
    url = "https://api.waifu.pics/sfw/waifu"
     r = requests.get(url)
     e = r.json()
    message.reply_photo(photo=e["url"])
