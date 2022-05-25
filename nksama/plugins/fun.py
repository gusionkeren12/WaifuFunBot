from pyrogram.types import Message
from pyrogram import filters
from nksama import bot

dnote = [ ]

deathnote_img = "https://telegra.ph/file/9e220eb59606f8435eafe.mp4"

@bot.on_message(filters.command('deathnote'))
def deathnote(_, m: Message):
    reply = m.reply_to_message
    if reply:
        dnote.append(reply.from_user.first_name)
        reply.reply_animation(deathnote_img,
                              caption="{} Added Death Note List!".format(reply.from_user.mention))
        
    else:
        m.reply_animation(deathnote_img,
                              caption="{} Added Death Note List!".format(m.from_user.mention))
  

@bot.on_message(filters.command('dlist'))
def dlist(_, m):
    reply = m.reply_to_message
    if reply:
        reply(str(dnote))
    else:
        m.reply(str(dnote))
