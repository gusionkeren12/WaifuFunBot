from nksama import bot
from pyrogram import filters


@bot.on_message(filters.text & filters.chat("@unitedsupport"))
def nevermind(_,message):
  if message.from_user.id == 1491497760 and "completed" in message.text:
    message.delete()
