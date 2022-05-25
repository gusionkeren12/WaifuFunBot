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
def ban(_,m: message):
    reply = message.reply_to_message
    if m.from_user.id in dev_user:
        bot.kick_chat_member(m.chat.id , reply.from_user.id)
        bot.send_message(m.chat.id ,f"Banned! {reply.from_user.mention}")
     else:
         m.reply("only Dev use this")
