import nekos.py

from nksama import bot 
from pyrogram import filters


bot.on. message(filters.command('waifu'))
def waifu(_,message):
    message.reply_photo(nekos.img(waifu))
