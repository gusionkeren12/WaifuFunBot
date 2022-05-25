from nksama import bot, dev_user
from pyrogram import filters
from pyrogram.types import Message

@bot.on_message(filters.command('ban'))
def ban(_,message):
    # scammer = reply.from_user.id
    reply = message.reply_to_message
    if is_admin(message.chat.id , message.from_user.id) and reply and reply.from_user.id not in dev_user and message.from_user.id != 825664681:
        bot.kick_chat_member(message.chat.id , message.reply_to_message.from_user.id)
        bot.send_message(message.chat.id ,f"Banned! {reply.from_user.username}")
