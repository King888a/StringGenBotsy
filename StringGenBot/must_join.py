from config import MUST_JOIN

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://telegra.ph/file/a5b1289136fb79f199b67.jpg", caption=f"» 𝖠𝖢𝖢𝖮𝖱𝖣𝖨𝖭𝖦 𝖳𝖮 𝖬𝖸 𝖣𝖠𝖳𝖠𝖡𝖠𝖲𝖤 𝖸𝖮𝖴'𝖵𝖤 𝖭𝖮𝖳 𝖩𝖮𝖨𝖭𝖤𝖣 [𝖣𝖤𝖵𝖨𝖫𝖲 𝖧𝖤𝖠𝖵𝖤𝖭]({link}) 𝖸𝖤𝖳, 𝖨𝖥 𝖸𝖮𝖴 𝖶𝖠𝖭𝖳 𝖳𝖮 𝖴𝖲𝖤 𝖬𝖤 𝖳𝖧𝖤𝖭 𝖩𝖮𝖨𝖭 [𝖣𝖤𝖵𝖨𝖫𝖲 𝖧𝖤𝖠𝖵𝖤𝖭]({link}) 𝖠𝖭𝖣 𝖲𝖳𝖠𝖱𝖳 𝖬𝖤 𝖠𝖦𝖠𝖨𝖭 !",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("</> 𝖣𝖤𝖵𝖨𝖫𝖲 𝖧𝖤𝖠𝖵𝖤𝖭", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MUST_JOIN chat : {MUST_JOIN} !")
