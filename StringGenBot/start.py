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

𝖳𝖧𝖨𝖲 𝖨𝖲 {me2},
𝖠𝖭 𝖮𝖯𝖤𝖭 𝖲𝖮𝖴𝖱𝖢𝖤 𝖲𝖤𝖲𝖲𝖨𝖮𝖭 𝖡𝖮𝖳 𝖦𝖤𝖭𝖤𝖱 𝖶𝖱𝖨𝖳𝖳𝖤𝖭 𝖨𝖭 𝖯𝖸𝖱𝖮𝖦𝖱𝖠𝖬

𝖬𝖠𝖣𝖤 𝖶𝖨𝖳𝖧 𝖡𝖸 ︙ [𝖲𝖮𝖱𝖴𝖢𝖤 𝖯𝖱𝖮𝖦𝖱𝖠𝖬𝖬𝖤𝖱](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="GEMERATE SESSION", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("𝖲𝖮𝖱𝖴𝖢𝖤 𝖣𝖱𝖠𝖦𝖮", url="https://github.com/qithoniq/StringGenBot"),
                    InlineKeyboardButton("𝖲𝖮𝖱𝖴𝖢𝖤 𝖯𝖱𝖮𝖦𝖱𝖠𝖬𝖬𝖤𝖱", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
