from nksama import bot 
from pyrogram import filters
import nekos.py

bot.on. message(filters.command('waifu'))
def hi(_,message):
    await message.reply_photo(nekos.img(waifu))
