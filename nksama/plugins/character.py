from nksama import bot
from pyrogram.types import Messages
from pyrogram import filters
import requests 

character_query = """
    query ($query: String) {
        Character (search: $query) {
               id
               name {
                     first
                     last
                     full
               }
               siteUrl
               image {
                        large
               }
               description
        }
    }
"""

url = 'https://graphql.anilist.co'

@bot.on_message(filters.command("character"))
async def character(_, m: Message):
        search = m.text.split(None, 1)[1]
        variables = {'search': search}
        json = requests.post(
        url, json={
            'query': character_query,
            'variables': variables
        }).json()
     if json:
        json = json['data']['Character']
        msg = f"*{json.get('name').get('full')}*(`{json.get('name').get('native')}`)\n"
        description = f"{json['description']}"
        site_url = json.get('siteUrl')
        msg += shorten(description, site_url)
        image = json.get('image', None)
        if image:
            image = image.get('large')
            await m.reply_photo(
                photo=image,
                caption=msg.replace('**', '**'),
