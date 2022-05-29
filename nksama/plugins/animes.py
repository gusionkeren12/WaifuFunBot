from nksama import bot
from pyrogram import *
from pyrogram.types import *


async def character(update: Update, context: CallbackContext):
    msg = update.effective_message
    res = ""
    args = context.args
    query = " ".join(args)
    try:
        search = jikan.search("character", query).get("results")[0].get("mal_id")
    except APIException:
        await msg.reply_text("No results found!")
        return ""
    if search:
        try:
            res = jikan.character(search)
        except APIException:
            await msg.reply_text("Error connecting to the API. Please try again!")
            return ""
    if res:
        name = res.get("name")
        kanji = res.get("name_kanji")
        about = res.get("about")
        about = re.sub(r"\\n", r"\n", about)
        about = re.sub(r"\r\n", r"", about)
        if len(about) > 4096:
            about = about[:4000] + "..."
        image = res.get("image_url")
        url = res.get("url")
        rep = f"<b>{name} ({kanji})</b>\n\n"
        rep += f"<a href='{image}'>\u200c</a>"
        rep += f"<i>{about}</i>"
        keyb = [
            [InlineKeyboardButton("More Information", url=url),
           InlineKeyboardButton("Add to favorite character", callback_data=f"xanime_fvrtchar={name}")]]
        
        
        await msg.reply_text(rep, parse_mode=ParseMode.HTML, reply_markup=InlineKeyboardMarkup(keyb))
        
