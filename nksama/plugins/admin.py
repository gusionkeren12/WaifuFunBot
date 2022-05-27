from nksama import bot,  dev_user
from nksama.config import BOT_ID
from pyrogram import filters
from pyrogram.types import Message
from nksama.utils.pluginshelper import extract_user

async def member_permissions(chat_id: int, user_id: int):
    perms = []
    try:
        member = await app.get_chat_member(chat_id, user_id)
    except Exception:
        return []
    if member.can_post_messages:
        perms.append("can_post_messages")
    if member.can_edit_messages:
        perms.append("can_edit_messages")
    if member.can_delete_messages:
        perms.append("can_delete_messages")
    if member.can_restrict_members:
        perms.append("can_restrict_members")
    if member.can_promote_members:
        perms.append("can_promote_members")
    if member.can_change_info:
        perms.append("can_change_info")
    if member.can_invite_users:
        perms.append("can_invite_users")
    if member.can_pin_messages:
        perms.append("can_pin_messages")
    if member.can_manage_voice_chats:
        perms.append("can_manage_voice_chats")
    return perms

from nksama.utils.permissions import adminsOnly


@bot.on_message(filters.command('ban'))
def ban(_, m: Message):
    reply = m.reply_to_message
    if m.from_user.id in dev_user:
        bot.ban_chat_member(m.chat.id , reply.from_user.id)
        bot.send_sticker(m.chat.id, sticker="CAACAgUAAx0CZMMuUQAC3OlikB7LsqnQNtRaqWaPBhN-mW29cwACNgMAAnzNrCRlyA3F-lEclh4E")
        bot.send_message(m.chat.id ,f"Banned! {reply.from_user.mention}")
    
    else:
        m.reply("`only Dev use this`")

        
@bot.on_message(filters.command('unban'))
def unban(_, m: Message):
    reply = m.reply_to_message
    if m.from_user.id in dev_user:
        bot.unban_chat_member(m.chat.id , reply.from_user.id)
        bot.send_message(m.chat.id ,f"Unbanned! {reply.from_user.mention}")
    
    else:
        m.reply("`only Dev use this`")

        
@bot.on_message(filters.command('kick'))
def kick(_, m: Message):
    reply = m.reply_to_message
    if m.from_user.id in dev_user:
            bot.ban_chat_member(m.chat.id , reply.from_user.id)
            bot.send_message(m.chat.id ,f"Kicked! {reply.from_user.mention}")
            bot.unban_chat_member(m.chat.id, reply.from_user.id)
    else:
        m.reply("`only Dev use this`")
        
        
@bot.on_message(filters.command('pin'))
def pin(_, m: Message):
    message_id = m.reply_to_message.id
    reply = m.reply_to_message
    if m.from_user.id in dev_user:
        bot.pin_chat_message(m.chat.id , message_id)
        bot.send_message(m.chat.id ,f"pinned by {m.from_user.mention}!")
    
    else:
        m.reply("`only Dev use this`")

        
@bot.on_message(filters.command('unpin'))
def unpin(_, m: Message):
    message_id = m.reply_to_message.id
    reply = m.reply_to_message
    if m.from_user.id in dev_user:
        bot.unpin_chat_message(m.chat.id , message_id)
        bot.send_message(m.chat.id ,f"unpinned by {m.from_user.mention}!")
    
    else:
       m.reply("`only Dev use this`")
    
@bot.on_message(filters.command("del"))
@adminsOnly("can_delete_messages")
async def deleteFunc(_, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("Reply To A Message To Delete It")
    await message.reply_to_message.delete()
    await message.delete()
    
@bot.on_message(filters.command("purge"))
@adminsOnly("can_delete_messages")
async def purgeFunc(_, message: Message):
    await message.delete()

    if not message.reply_to_message:
        return await message.reply_text("Reply to a message to purge from.")

    chat_id = message.chat.id
    message_ids = []

    for message_id in range(
        message.reply_to_message.id,
        message.id,
    ):
        message_ids.append(message_id)

        # Max message deletion limit is 100
        if len(message_ids) == 100:
            await bot.delete_messages(
                chat_id=chat_id,
                message_ids=message_ids,
                revoke=True,  # For both sides
            )

            # To delete more than 100 messages, start again
            message_ids = []

    # Delete if any messages left
    if len(message_ids) > 0:
        await bot.delete_messages(
            chat_id=chat_id,
            message_ids=message_ids,
            revoke=True,
        )
 

@bot.on_message(filters.command('promote'))
@adminsOnly("can_promote_members")
async def promote(_, m: Message):
    reply = m.reply_to_message
    await bot.promote_chat_member(m.chat.id , reply.from_user.id)
    await bot.send_message(m.chat.id ,f"Admin: {m.from_user.mention}\npromoted! {reply.from_user.mention}")
         
        
