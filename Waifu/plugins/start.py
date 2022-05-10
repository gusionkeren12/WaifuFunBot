from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from Waifu import bot
from pyrogram import filters 
from nksama import help_message


@bot.on_message(filters.command('start'))
def start(_,message):

    bot.send_message(message.chat.id , "Hello there! \nI'll help you to enjoy your groups" , reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton('[ help ]' , callback_data="help")]
    ]))
