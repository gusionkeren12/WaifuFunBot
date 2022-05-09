from nksama import bot , help_message
from pyrogram import filters

bot.on. message(filters.command('hi'))
def hi(_,message):
  message.reply('hi')
