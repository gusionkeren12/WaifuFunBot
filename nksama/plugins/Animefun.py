from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from nksama import bot
from pyrogram import filters
import requests, nekos
from nksama import help_message 
from pyrogram.types import Message
from nksama.plugins.helpers import call_back_in_filter


@bot.on_message(filters.command('wink'))
def wink(_,message):
    reply = message.reply_to_message
    if reply:
        res = requests.get('https://some-random-api.ml/animu/wink').json()
        url = res['link']
        reply.reply_animation(url)
        
    else:
        message.reply_animation(url)
        
        
@bot.on_message(filters.command('hug'))
def hug(_,message):
    reply = message.reply_to_message
    if reply:
        res = requests.get('https://some-random-api.ml/animu/hug').json()
        url = res['link']
        reply.reply_animation(url)
        
    else:
        message.reply_animation(url)

@bot.on_message(filters.command('pat'))
def pat(_,message):
    reply = message.reply_to_message
    if reply:
        res = requests.get('https://some-random-api.ml/animu/pat').json()
        url = res['link']
        reply.reply_animation(url)
        
    else:
        message.reply_animation(url)
        

@bot.on_message(filters.command("waifu"))
async def waifu(bot, m: Message):
      await m.reply_photo(nekos.img("waifu"))
        
 
@bot.on_message(filters.command("hmeme"))
async def hmeme(bot, m: Message):
          res = requests.get('https://nksamamemeapi.pythonanywhere.com').json()
          img = res['image']
          title = res['title"]
      await m.reply_photo(img, caption=title)
        
