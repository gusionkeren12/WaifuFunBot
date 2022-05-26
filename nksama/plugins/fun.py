from pyrogram.types import Message
from pyrogram import filters
from nksama import bot

dnote = [ ]

deathnote_img = "https://telegra.ph/file/9e220eb59606f8435eafe.mp4"

@bot.on_message(filters.command('adddeathnote'))
def adddeathnote(_, m: Message):
    reply = m.reply_to_message
    if reply:
        dnote.append(reply.from_user.first_name)
        reply.reply_animation(deathnote_img,
                              caption="{} Added Death Note List!".format(reply.from_user.mention))
        
    else:
        m.reply_animation(deathnote_img,
                              caption="{} Added Death Note List!".format(m.from_user.mention))
  
@bot.on_message(filters.command('removedeathnote'))
def removedeathnote(_, m: Message):
    reply = m.reply_to_message
    if reply:
        dnote.remove(reply.from_user.first_name)
        reply.reply_animation(deathnote_img,
                              caption="{} Removed Death Note List!".format(reply.from_user.mention))
        
    else:
        m.reply("reply to Death Note list added person!")
  

@bot.on_message(filters.command('deathnotelist'))
def deathnotelist(_, m):
    reply = m.reply_to_message
    if reply:
        reply(str(dnote))
    else:
        m.reply(str(dnote))
        
        
@bot.on_message(filters.regex('good morning'))
def gm(_, m: Message):
    reply = m.reply_to_message
    if reply:
        reply(f"good morning! {reply.from_user.mention}")
    else:
        reply(f"good morning! {m.from_user.mention}")
 

@bot.on_message(filters.regex('good night'))
def gn(_, m: Message):
    reply = m.reply_to_message
    if reply:
        reply(f"good night! {reply.from_user.mention}")
    else:
        reply(f"good night! {m.from_user.mention}")
        
        
