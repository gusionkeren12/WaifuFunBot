import requests

from nksama import bot 
from pyrogram import filters


bot.on. message(filters.command('waifu'))
def waifu(_,message):
    url = "https://api.waifu.pics/sfw/waifu"
     r = requests.get(url)
     e = r.json()
  await bot.send_photo(message.chat.id, photo=e["url"], caption="Waifu images 💕💕")
