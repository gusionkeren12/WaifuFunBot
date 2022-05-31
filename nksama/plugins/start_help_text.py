from pyrogram import filters
import random 
from pyrogram.types import Message
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from nksama import bot, SUPPORT_CHAT
from pyrogram.types import CallbackQuery


           
BOT_IMG = [ "https://telegra.ph/file/b3fbf990e0b67ede241a3.jpg",
           "https://telegra.ph/file/94865dae2576a2fa52732.jpg" ]
text = """
Hello! Dear {}

I'm An Anime themed Smart VegetaRobot make your group's
joyful Using /help commands!!

powered by @PegaBots
"""


@bot.on_message(filters.command(["start"], ["/", ".", "?"]))
async def start(_, m: Message):
    buttons = [
        [
            InlineKeyboardButton(
                "ADD ME", url="t.me/VegetaRobot?startgroup=true"),
            InlineKeyboardButton(
                "help", callback_data='_help'),]]

    await m.reply_photo(
        random.choice(BOT_IMG),
        caption=text.format(m.from_user.mention),
        reply_markup=InlineKeyboardMarkup(buttons),
    )

          
HELP_TEXT = """
Hello! Dear {}

here my help and commands list! 

• /animehelp - for my anime commands list!
• /devhelp - for my developer commands list! 
"""
         
@bot.on_message(filters.command(["help"], ["/", ".", "?"]))
async def start(_, m: Message):
   
       await m.reply_text(HELP_TEXT.format(m.from_user.mention))
           
  
ANIME_TEXT = """

hello! Dear {}

here the anime help & commads

• /neko - 
"""

@bot.on_callback_query(filters.regex("_help"))
async def help_back(query: CallbackQuery, message):
    await query.message.edit_caption("test man")
               
        
