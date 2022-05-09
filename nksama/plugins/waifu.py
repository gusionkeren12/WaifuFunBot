import requests

from nksama import bot 
from pyrogram import filters


bot.on. message(filters.command('waifu'))
def waifu(_,message):
    res = requests.get('https://some-random-api.ml/animu/pat').json()
      
  await bot.send_photo(message.chat.id, photo=e["url"], caption="Waifu images 💕💕")
