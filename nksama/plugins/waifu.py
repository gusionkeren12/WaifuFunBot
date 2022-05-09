import requests

from nksama import bot 
from pyrogram import filters


bot.on. message(filters.command('waifu'))
def waifu(_,message):
     reply = message.reply_to_message
    if reply:
        res = requests.get('"https://api.waifu.pics/sfw/waifu').json()
        url = res['link']
        reply.reply_photo(url)
          
       else:
         message.reply_animation(url)
        
    
