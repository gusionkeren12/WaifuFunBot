from pyrogram import filters
from pyrogram.types import Message
from nksama import bot

@bot.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
        await m.reply("hello! {} Welcome to **{}**".format(m.from_user.mention,m.chat.title)
