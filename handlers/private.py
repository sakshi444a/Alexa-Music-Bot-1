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
        caption=f"""**𝐓𝐡𝐢𝐬 𝐈𝐬 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 🥀𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 🎶 𝐁𝐨𝐭 𝐑𝐮𝐧 𝐎𝐧 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 🥀 𝐕𝐩𝐬 💫𝐒𝐞𝐫𝐯𝐞𝐫 🌎 𝐅𝐞𝐞𝐥 ❤️ 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐌𝐮𝐬𝐢𝐜 🎧 𝐈𝐧 𝐕𝐜 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 = [𝗦𝗺𝗼𝗞𝗲𝗿'𝘅𝗗 🚬❤️](https://t.me/sanki_owner)

🇴ᴡɴᴇʀ :- [Sᴜᴍɪᴛ Yᴀᴅᴀᴠ](https://t.me/Simple_Mundaa)
🇸ᴜᴘᴘᴏʀᴛ 🇬ʀᴏᴜᴘ   » [Wᴏʀʟᴅ FʀɪᴇɴᴅSʜɪᴘ Zᴏɴᴇ](https://t.me/World_FriendShip_Zone)
🇩ɪsᴄᴜss 🇬ʀᴏᴜᴘ  » [Dᴇᴍᴏɴ Cʀᴇᴀᴛᴏʀs Sᴜᴘᴘᴏʀᴛ](https://t.me/Demon_Creators_Support)
🇾ᴏᴜᴛᴜʙᴇ 🇨ʜᴀɴɴᴇʟ   » [ᴀs ᴛᴇᴄʜɴɪᴄᴀʟ](https://youtube.com/channel/UCtI7hbY-BD7wvuIzoSU0cEw)
🇫ᴇᴍᴀʟᴇ 🇴ᴡɴᴇʀ  » [Nɪᴋɪᴛᴀ](https://t.me/Cute_Shezhadi012)
🇺ᴘᴅᴀᴛᴇ 🇨ʜᴀɴɴᴇʟ  » [Dᴇᴍᴏɴ Cʀᴇᴀᴛᴏʀs](https://t.me/Demon_Creators)

ɪғ ʏᴏᴜ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴀɴᴅ ɪssᴜᴇ sᴏ ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇsᴇ ɪᴅ = [Sᴜᴍɪᴛ Yᴀᴅᴀᴠ](https://t.me/Simple_Mundaa)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🅳︎ɪsʜɴᴇʏ xᴅ 🅷︎ᴇᴀʀᴛ", url=f"https://t.me/DISNEY_XD_HEART")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo", "channel"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/10d469ec236d49a43650c.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ʀᴇᴘᴏ ᴀᴘᴘᴇᴀʟ ᴏɴ ᴛʜᴇsᴇ ɢʀᴏᴜᴘ ", url=f"https://t.me/Demon_Creators_Support")
                ]
            ]
        ),
    )
