import requests
import nekos
from PIL import Image
import os

from nksama import bot
from pyrogram import filters
from pyrogram.types import Message

@bot.on_message(filters.command("neko"))
def neko(_,  m: Message):
    target = "neko"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("feet"))
def feet(_,  m: Message):
    target = "feet"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("yuri"))
def yuri(_,  m: Message):
    target = "yuri"
    m.reply_photo(nekos.img(target))

@bot.on_message(filters.command("trap"))
def trap(_,  m: Message):
    target = "trap"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("futanari"))
def futanari(_,  m: Message):
    target = "futanari"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("hololewd"))
def hololewd(_,  m: Message):
    target = "hololewd"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("lewdkemo"))
def lewdkemo(_,  m: Message):
    target = "lewdkemo"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("solog"))
def sologif(_,  m: Message):
    target = "solog"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("feetgv"))
def feetgif(_,  m: Message):
    target = "feetg"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("cum"))
def cumgif(_,  m: Message):
    target = "cum"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("erokemo"))
def erokemo(_,  m: Message):
    target = "erokemo"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("les"))
def lesbian(_,  m: Message):
    target = "les"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("wallpaper"))
def wallpaper(_,  m: Message):
    target = "wallpaper"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("lewdk"))
def lewdk(_,  m: Message):
    target = "lewdk"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("ngif"))
def ngif(_,  m: Message):
    target = "ngif"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("tickle"))
def tickle(_,  m: Message):
    target = "tickle"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("lewd"))
def lewd(_,  m: Message):
    target = "lewd"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("feed"))
def feed(_,  m: Message):
    target = "feed"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("eroyuri"))
def eroyuri(_,  m: Message):
    target = "eroyuri"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("eron"))
def eron(_,  m: Message):
    target = "eron"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("cumjpg"))
def cum(_,  m: Message):
    target = "cum_jpg"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("bj"))
def bjgif(_,  m: Message):
    target = "bj"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("blowjob"))
def bj(_,  m: Message):
    target = "blowjob"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("nekonsfw"))
def nekonsfw(_,  m: Message):
    target = "nsfw_neko_gif"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("solo"))
def solo(_,  m: Message):
    target = "solo"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("kemonomimi"))
def kemonomimi(_,  m: Message):
    target = "kemonomimi"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("avatarlewd"))
def avatarlewd(_,  m: Message):
    target = "nsfw_avatar"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    m.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")


@bot.on_message(filters.command("gasm"))
def gasm(_,  m: Message):
    target = "gasm"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    m.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")


@bot.on_message(filters.command("poke"))
def poke(_,  m: Message):
    target = "poke"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("anal"))
def anal(_,  m: Message):
    target = "anal"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("hentai"))
def hentai(_,  m: Message):
    target = "hentai"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("avatar"))
def avatar(_,  m: Message):
    target = "nsfw_avatar"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    m.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")


@bot.on_message(filters.command("erofeet"))
def erofeet(_,  m: Message):
    target = "erofeet"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("holo"))
def holo(_,  m: Message):
    target = "holo"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("keta"))
def keta(_,  m: Message): 
     target = 'keta'
     if not target:
         m.reply_text("No URL was received from the API!")
         return
     m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("pussy"))
def pussygif(_,  m: Message):
    target = "pussy"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("tits"))
def tits(_,  m: Message):
    target = "tits"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("holoero"))
def holoero(_,  m: Message):
    target = "holoero"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("pussyjpg"))
def pussy(_,  m: Message):
    target = "pussy_jpg"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("hentaigif"))
def hentaigif(_,  m: Message):
    target = "random_hentai_gif"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("classic"))
def classic(_,  m: Message):
    target = "classic"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("kuni"))
def kuni(_,  m: Message):
    target = "kuni"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("waifu"))
def waifu(_,  m: Message):
    target = "waifu"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    m.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")


@bot.on_message(filters.command("kiss"))
def kiss(_,  m: Message):
    target = "kiss"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("femdom"))
def femdom(_,  m: Message):
    target = "femdom"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("cuddle"))
def cuddle(_,  m: Message):
    target = "cuddle"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("erok"))
def erok(_,  m: Message):
    target = "erok"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("foxgirl"))
def foxgirl(_,  m: Message):
    target = "fox_girl"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("boobs"))
def titsgif(_,  m: Message):
    target = "boobs"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("ero"))
def ero(_,  m: Message):
    target = "ero"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("smug"))
def smug(_,  m: Message):
    target = "smug"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("baka"))
def baka(_,  m: Message):
    target = "baka"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("dva"))
def dva(_,  m: Message):

    nsfw = requests.get("https://api.computerfreaker.cf/v1/dva").json()
    url = nsfw.get("url")
    # do shit with url if you want to
    if not url:
        m.reply_text("No URL was received from the API!")
        return
    m.reply_photo(url)
    
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
