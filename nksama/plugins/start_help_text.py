from pyrogram import filters
import random 
from pyrogram.types import Message
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from nksama import bot, SUPPORT_CHAT



           
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
                "help", callback_data='help'),]]

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

       await query.answer('help')
    elif query.data == "help":
        buttons = [[
            InlineKeyboardButton('𝘼𝙙𝙢𝙞𝙣', callback_data='admin'),
            InlineKeyboardButton('𝘾𝙤𝙣𝙣𝙚𝙘𝙩', callback_data='coct'),
            InlineKeyboardButton('𝙁𝙞𝙡𝙩𝙚𝙧𝙨', callback_data='auto_manual')
            ],[
            InlineKeyboardButton('𝘾𝙤𝙫𝙞𝙙', callback_data='covid'),
            InlineKeyboardButton('𝙂𝙩𝙧𝙖𝙣𝙨', callback_data='gtrans'),
            InlineKeyboardButton('𝙄𝙣𝙛𝙤', callback_data='info')
            ],[
            InlineKeyboardButton('𝙄𝙣𝙡𝙞𝙣𝙚', callback_data='inline'),
            InlineKeyboardButton('𝙈𝙚𝙢𝙚𝙨', callback_data='memes'),
            InlineKeyboardButton('𝙈𝙪𝙨𝙞𝙘', callback_data='music')
            ],[
            InlineKeyboardButton('𝙋𝙖𝙨𝙨𝙬𝙤𝙧𝙙', callback_data='genpassword'),
            InlineKeyboardButton('𝙋𝙖𝙨𝙩𝙚', callback_data='paste'),
            InlineKeyboardButton('𝙋𝙞𝙣', callback_data='pin')
            ],[
            InlineKeyboardButton('𝙋𝙪𝙧𝙜𝙚', callback_data='purge'),
            InlineKeyboardButton('𝙍𝙚𝙨𝙩𝙧𝙞𝙘𝙩', callback_data='restric'),
            InlineKeyboardButton('𝙎𝙚𝙖𝙧𝙘𝙝', callback_data='search')
            ],[
            InlineKeyboardButton('𝙎𝙝𝙖𝙧𝙚 𝙏𝙚𝙭𝙩', callback_data='sharetext'),
            InlineKeyboardButton('𝙎𝙩𝙞𝙘𝙠𝙚𝙧 𝙄𝘿', callback_data='stickerid'),
            InlineKeyboardButton('𝙎𝙪𝙙𝙤', callback_data='admin')
            ],[
            InlineKeyboardButton('𝙏𝙏𝙎', callback_data='tts'),
            InlineKeyboardButton('𝙏𝙂𝙧𝙖𝙥𝙝', callback_data='tgraph'),
            InlineKeyboardButton('𝙏𝙤𝙧𝙧𝙚𝙣𝙩', callback_data='torrent')
            ],[
            InlineKeyboardButton('𝙐𝙧𝙡 𝙎𝙝𝙤𝙧𝙩𝙚𝙧', callback_data='shortner'),
            InlineKeyboardButton('🔰𝙎𝙩𝙖𝙩𝙪𝙨', callback_data='stats'),
            InlineKeyboardButton('𝙕𝙤𝙢𝙗𝙞𝙚𝙨', callback_data='zombies')
            ],[
            InlineKeyboardButton('𝙎𝙤𝙪𝙧𝙘𝙚', callback_data='source'),
            InlineKeyboardButton('« 𝘽𝙖𝙘𝙠', callback_data='start'),
            InlineKeyboardButton('𝘼𝙗𝙤𝙪𝙩', callback_data='about')
        ]]
           
