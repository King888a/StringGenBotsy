from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""Hᴇʏ {msg.from_user.mention},

Tʜɪs ɪs {me2},
AN OPEN SOURCE STRING SESSION BOT  GENERATOR,WRITTEN IN PYROGRAM .

Mᴀᴅᴇ ᴡɪᴛʜ 🖤 ʙʏ : [𝝙𝗡𝗢𝗡𝗬𝗠𝗢𝗨𝗦](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="GEMERATE SESSION", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("𝐒𝐨𝐮𝐫𝐜𝐞 𝐃𝐫𝐚𝐠𝐨", url="https://github.com/qithoniq/StringGenBot"),
                    InlineKeyboardButton("Source programmer", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
