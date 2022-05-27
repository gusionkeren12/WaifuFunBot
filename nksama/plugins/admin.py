from nksama import bot, dev_user
from pyrogram import filters
from pyrogram.types import Message

def is_admin(group_id: int, user_id: int):
    try:
        user_data = bot.get_chat_member(group_id, user_id)
        if user_data.status == 'administrator' or user_data.status == 'creator':
            # print(f'is admin user_data : {user_data}')
            return True
        else:
            # print('Not admin')
            return False
    except:
        # print('Not admin')
        return False


@bot.on_message(filters.command('ban'))
def ban(_, m: Message):
    reply = m.reply_to_message
    if m.from_user.id in dev_user:
        bot.ban_chat_member(m.chat.id , reply.from_user.id)
        bot.send_sticker(m.chat.id, sticker="CAACAgUAAx0CZMMuUQAC3OlikB7LsqnQNtRaqWaPBhN-mW29cwACNgMAAnzNrCRlyA3F-lEclh4E")
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
    message_id = m.reply_to_message.id
    reply = m.reply_to_message
    if m.from_user.id in dev_user:
        bot.pin_chat_message(m.chat.id , message_id)
        bot.send_message(m.chat.id ,f"pinned by {m.from_user.mention}!")
    
    else:
        m.reply("`only Dev use this`")

        
@bot.on_message(filters.command('unpin'))
def unpin(_, m: Message):
    message_id = m.reply_to_message.id
    reply = m.reply_to_message
    if m.from_user.id in dev_user:
        bot.unpin_chat_message(m.chat.id , message_id)
        bot.send_message(m.chat.id ,f"unpinned by {m.from_user.mention}!")
    
    else:
        m.reply("`only Dev use this`")

        
