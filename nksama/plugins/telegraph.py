from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup



@bot.on_message(filters.command('start'))
def start(_,message):

    bot.send_photo(message.chat.id ,photo="https://telegra.ph/file/0f4b6a40dc4eb52587234.jpg",caption="Hello there i'm Yuuki-San\nI'll help you to manage your groups" , reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton('[ help ]' , callback_data="help")]
    ]))
from nksama import bot as app, telegraph


@app.on_message(filters.command("telegraph"))
async def paste(_, message: Message):
    reply = message.reply_to_message

    if not reply or not reply.text:
        return await message.reply("Reply to a text message")

    if len(message.command) < 2:
        return await message.reply("**Usage:**\n /telegraph [Page name]")

    page_name = message.text.split(None, 1)[1]
    page = telegraph.create_page(
        page_name, html_content=(reply.text.html).replace("\n", "<br>")
    )
    return await message.reply(
        f"**Posted:** {page['url']}",reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton('View 💫' , url=f"{page['url']}")]
    ]))
        
