import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/10d469ec236d49a43650c.jpg",
        caption=f"""**ᴛʜɪs ᴍᴜsɪᴄ ʙᴏᴛ ɪs ᴛʜᴇ ɴᴇxᴛ ʟᴇᴠᴇʟ ᴏғ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴛʜᴀᴛ ʜᴀs ʙᴇsᴛ ʜɪɢʜ ǫᴜᴀʟɪᴛʏ ᴏғ ᴍᴜsɪᴄ ʙᴏᴛ ᴀɴᴅ ᴛʜᴇ ᴛʜɪs ᴍᴜsɪᴄ ʙᴏᴛ sᴍᴀsʜ ᴛʜᴇᴍ ᴏғ ᴀʟʟ sᴇʀᴠᴇʀ ᴏғ ᴍᴜsɪᴄ ʙᴏᴛ ᴀss...

🇴ᴡɴᴇʀ :- [Yᴀsʜ ʀᴀᴊ](https://t.me/give_up_to_god)

🇫ᴇᴍᴀʟᴇ 🇴ᴡɴᴇʀ  » [Sᴀᴋsʜɪ](https://t.me/ABOUTDIEDINSAAN)

ɪғ ʏᴏᴜ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴀɴᴅ ɪssᴜᴇ sᴏ ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇsᴇ ɪᴅ = [ʏᴀsʜ ʀᴀᴊ](https://t.me/give_up_to_god)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🅹ᴏɪɴ 🅷ᴇʀᴇ", url=f"https://t.me/ASERNIC_SUPPORT")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["sakshi", "yash"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/10d469ec236d49a43650c.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ʀᴇᴘᴏ ᴀᴘᴘᴇᴀʟ ᴏɴ ᴛʜᴇsᴇ ɢʀᴏᴜᴘ ", url=f"https://t.me/ASERNIC_SUPPORT")
                ]
            ]
        ),
    )
