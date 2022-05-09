import requests

from nksama import bot 
from pyrogram import filters

        
    
@bot.on_message(filters.command('waifu'))
def waifu(_,message):
    reply = message.reply_to_message
    if reply:
        res = requests.get("https://api.waifu.pics/sfw/waifu").json()
        
        reply.reply_photo(res)
        
    else:
        message.reply_photo(res)
