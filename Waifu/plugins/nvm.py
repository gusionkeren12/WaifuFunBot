from Waifu import bot
from pyrogram import filters


@bot.on_message(filters.text & filters.chat(-1001590378481))
def nevermind(_,message):
  if message.from_user.id == 1491497760 and "punda" in message.text:
    message.delete()
