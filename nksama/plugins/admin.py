from nksama import bot, dev_user
from pyrogram import filters
from pyrogram.types import Message

@bot.on_message(filters.command('ban'))
def ban(_, m: Message):
    reply = m.reply_to_message
    if m.from_user.id in dev_user:
        bot.ban_chat_member(m.chat.id , reply.from_user.id)
        bot.send_message(m.chat.id ,f"Banned! {reply.from_user.mention}")
    
    else:
        m.reply("`only Dev use this`")

        
@bot.on_message(filters.command('unban'))
def unban(_, m: Message):
    reply = m.reply_to_message
    if m.from_user.id in dev_user:
        bot.unban_chat_member(m.chat.id , reply.from_user.id)
        bot.send_message(m.chat.id ,f"Unbanned! {reply.from_user.mention}")
    
    else:
        m.reply("`only Dev use this`")

        
@bot.on_message(filters.command('kick'))
def kick(_, m: Message):
    reply = m.reply_to_message
    if m.from_user.id in dev_user:
        bot.ban_chat_member(m.chat.id , reply.from_user.id)
        bot.send_message(m.chat.id ,f"Kicked! {reply.from_user.mention}")
        bot.unban_chat_member(m.chat.id, reply.from_user.id)
    else:
        m.reply("`only Dev use this`")
        
        
@bot.on_message(filters.command('pin'))
def pin(_, m: Message):
    reply = m.reply_to_message
    message_id = m.reply_to_message.message_id
       await bot.send_message("`Only Dev can Use this`")
     if m.from_user.id in dev_user:
      bot.pin_chat_message(m.chat.id , message_id)
      bot.send_message(m.chat.id,
         f"message pinned! [link](t.me/-{m.chat.id}/{message_id})\nAdmin: {m.from_user.mention}")
                 
    else:
        m.reply('Reply to a message')
