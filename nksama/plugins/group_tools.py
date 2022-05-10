
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from nksama import bot
from pyrogram import filters 
from nksama import help_message


@bot.on_message(filters.command('start'))
def start(_,message):

    bot.send_photo(message.chat.id ,photo="https://telegra.ph/file/0f4b6a40dc4eb52587234.jpg",caption="Hello there i'm Yuuki-San\nI'll help you to manage your groups" , reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton('[ help ]' , callback_data="help")]
    ]))
    
    
@bot.on_message(filters.command('id'))
def ids(_,message):
  reply = message.reply_to_message
  if reply:
    message.reply_text(f"**Your id**: {message.from_user.id}\n**User id**: {reply.from_user.id}\n**chat id**: {message.chat.id}")
  else:
    message.reply(f"**Your id**: {message.from_user.id}\n**chat id**: {message.chat.id}")