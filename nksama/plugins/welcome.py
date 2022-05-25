from pyrogram import filters
from pyrogram.types import Message
from nksama import bot

@bot.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
        await m.reply("hello! dear {}\nWelcome to **{}**".format(m.from_user.mention,m.chat.title))
        
@bot.on_message(filters.left_chat_member)
async def welcome(_, m: Message):
        await m.reply("oof! dear {}\nlefted to **{}**".format(m.from_user.mention,m.chat.title))
