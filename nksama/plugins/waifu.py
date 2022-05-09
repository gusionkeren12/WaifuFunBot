import requests

from nksama import bot 
from pyrogram import filters

        
    
@bot.on_message(filters.command('waifu'))
def waifu(_,message):
    x = requests.get("https://api.waifu.pics/sfw/waifu").json()
    await bot.message_photo(message.chat_id,photo=x)    
     
