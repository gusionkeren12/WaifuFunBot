from nksama import bot, dev_user
from pyrogram import filters
from pyrogram.types import Message

@bot.on_message(filters.command('ban'))
def ban(_, m: Message):
    reply = m.reply_to_message
    if m.from_user.id in dev_user:
        bot.kick_chat_member(m.chat.id , reply.from_user.id)
        bot.send_message(m.chat.id ,f"Banned! {reply.from_user.mention}")
    
    else:
        m.reply("only Dev use this")
