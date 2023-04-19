from pyrogram.types import Message
from telethon import TelegramClient
from pyrogram import Client, filters
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

import config



ask_ques = "**❲ 𝖯𝖫𝖤𝖠𝖲𝖤 𝖢𝖧𝖮𝖮𝖲𝖤 𝖳𝖧𝖤 𝖯𝖸𝖳𝖧𝖮𝖭 𝖫𝖨𝖡𝖱𝖠𝖱𝖸 𝖥𝖮𝖱 𝖶𝖧𝖨𝖢𝖧 𝖸𝖮𝖴 𝖶𝖠𝖭𝖳 𝖳𝖮 𝖦𝖤𝖭𝖤𝖱𝖠𝖳𝖤 𝖲𝖳𝖱𝖨𝖭𝖦 ❳**"
buttons_ques = [
    [
        InlineKeyboardButton("❲ 𝖯𝖸𝖱𝖮𝖦𝖱𝖠𝖬 ❳", callback_data="pyrogram"),
        InlineKeyboardButton("❲ 𝖳𝖤𝖫𝖤𝖳𝖧𝖮𝖭 ❳", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("❲ 𝖯𝖸𝖱𝖮𝖦𝖱𝖠𝖬 𝖡𝖮𝖳 ❳", callback_data="pyrogram_bot"),
        InlineKeyboardButton("❲ 𝖳𝖤𝖫𝖤𝖳𝖧𝖮𝖭 𝖡𝖮𝖳 ❳", callback_data="telethon_bot"),
    ],
]

gen_button = [
    [
        InlineKeyboardButton(text="❲ 𝖦𝖤𝖭𝖤𝖱𝖠𝖳𝖤 𝖲𝖤𝖲𝖲𝖨𝖮𝖭 ❳", callback_data="generate")
    ]
]




@Client.on_message(filters.private & ~filters.forwarded & filters.command(["generate", "gen", "string", "str"]))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, is_bot: bool = False):
    if telethon:
        ty = "𝖳𝖤𝖫𝖤𝖳𝖧𝖮𝖭"
    else:
        ty = "𝖯𝖸𝖱𝖮𝖦𝖱𝖠𝖬"
    if is_bot:
        ty += " 𝖡𝖮𝖳"
    await msg.reply(f"» 𝖳𝖱𝖸𝖨𝖭𝖦 𝖳𝖮 𝖲𝖳𝖠𝖱𝖳 **{ty}** 𝖲𝖤𝖲𝖲𝖨𝖮𝖭 𝖦𝖤𝖭𝖤𝖱𝖠𝖳𝖮𝖱...")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, "𝖯𝖫𝖤𝖠𝖲𝖤 𝖲𝖤𝖭𝖣 𝖸𝖮𝖴𝖱 𝖠𝖯𝖨_𝖨𝖣 𝖳𝖮 𝖯𝖱𝖮𝖢𝖤𝖤𝖣.\n\nᴄ𝖫𝖨𝖢𝖪 /skip 𝖥𝖮𝖱 𝖴𝖲𝖨𝖭𝖦 𝖡𝖮𝖳'𝖲 𝖠𝖯𝖨", filters=filters.text)
    if await cancelled(api_id_msg):
        return
    if api_id_msg.text == "/skip":
        api_id = config.API_ID
        api_hash = config.API_HASH
    else:
        try:
            api_id = int(api_id_msg.text)
        except ValueError:
            await api_id_msg.reply("**𝖠𝖯𝖨_𝖨𝖣** 𝖬𝖴𝖲𝖳 𝖡𝖤 𝖠𝖭 𝖨𝖭𝖳𝖤𝖦", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
            return
        api_hash_msg = await bot.ask(user_id, "❲ 𝖭𝖮𝖶 𝖯𝖫𝖤𝖠𝖲𝖤 𝖲𝖤𝖭𝖣 𝖸𝖮𝖴𝖱 𝖠𝖯𝖨_𝖧𝖠𝖲𝖧 𝖳𝖮 𝖢𝖮𝖭𝖳𝖨𝖭𝖴𝖤 ❳", filters=filters.text)
        if await cancelled(api_hash_msg):
            return
        api_hash = api_hash_msg.text
    if not is_bot:
        t = "❲ 𝖯𝖫𝖤𝖲𝖤 𝖲𝖤𝖭𝖣 𝖸𝖮𝖴𝖱 𝖯𝖧𝖮𝖭𝖤_𝖭𝖴𝖬𝖡𝖤𝖱 𝖶𝖨𝖳𝖧 𝖢𝖮𝖭𝖳𝖱𝖸 𝖢𝖮𝖣𝖤 𝖥𝖮𝖱 𝖶𝖧𝖨𝖢𝖧 𝖸𝖮𝖴 𝖶𝖠𝖭𝖳 𝖳𝖮 𝖦𝖤𝖭𝖤𝖱𝖠𝖳𝖤 𝖲𝖤𝖲𝖲𝖨𝖮𝖭 \n𝖤𝖷𝖠𝖬𝖯𝖨𝖤︙ +910000000000 ❳"
    else:
        t = "❲ 𝖯𝖫𝖤𝖠𝖲𝖤 𝖲𝖤𝖭𝖣 𝖸𝖮𝖴𝖱 𝖡𝖮𝖳_𝖳𝖮𝖪𝖤𝖭 𝖳𝖮.\n𝖤𝖷𝖠𝖬𝖯𝖨𝖤︙ 5432198765:abcdanonymousterabaalol ❳"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("❲ 𝖳𝖱𝖸𝖨𝖭𝖦 𝖳𝖮 𝖲𝖤𝖭𝖣 𝖮𝖳𝖯 𝖠𝖳 𝖳𝖧𝖤 𝖦𝖨𝖵𝖤𝖭 𝖭𝖴𝖬𝖡𝖤𝖱 ❳")
    else:
        await msg.reply("❲ 𝖳𝖱𝖸𝖨𝖭𝖦 𝖳𝖮 𝖫𝖮𝖦𝖨𝖭 𝖵𝖨𝖠 𝖳𝖮𝖪𝖤𝖭 ❳")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError):
        await msg.reply("» ʏᴏᴜʀ **ᴀᴩɪ_ɪᴅ** ᴀɴᴅ **ᴀᴩɪ_ʜᴀsʜ** ᴄᴏᴍʙɪɴᴀᴛɪᴏɴ ᴅᴏᴇsɴ'ᴛ ᴍᴀᴛᴄʜ ᴡɪᴛʜ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴩᴩs sʏsᴛᴇᴍ. \n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await msg.reply("» ᴛʜᴇ **ᴩʜᴏɴᴇ_ɴᴜᴍʙᴇʀ** ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ᴅᴏᴇsɴ'ᴛ ʙᴇʟᴏɴɢ ᴛᴏ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "❲ 𝖯𝖫𝖤𝖠𝖲𝖤 𝖲𝖤𝖭𝖣 𝖳𝖧𝖤 𝖮𝖳𝖯 𝖳𝖧𝖠𝖳 𝖸𝖮𝖴'𝖵𝖤 𝖱𝖤𝖢𝖤𝖨𝖵𝖤𝖣 𝖥𝖱𝖮𝖬 𝖳𝖤𝖫𝖤𝖳𝖧𝖮𝖭 𝖮𝖭  𝖸𝖮𝖴𝖱 𝖠𝖢𝖢𝖮𝖴𝖭𝖳.\n𝖨𝖥 𝖮𝖳𝖯 𝖨𝖲 `1 2 3 4 5` ❳", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply("» ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 10 ᴍɪɴᴜᴛᴇs.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError):
            await msg.reply("» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs **ᴡʀᴏɴɢ.**\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError):
            await msg.reply("» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs **ᴇxᴩɪʀᴇᴅ.**\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError):
            try:
                two_step_msg = await bot.ask(user_id, "» ᴩʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ **ᴛᴡᴏ sᴛᴇᴩ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ** ᴩᴀssᴡᴏʀᴅ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.", filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply("» ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 5 ᴍɪɴᴜᴛᴇs.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError):
                await two_step_msg.reply("» ᴛʜᴇ ᴩᴀssᴡᴏʀᴅ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs ᴡʀᴏɴɢ.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"**❲ 𝖳𝖧𝖨𝖲 𝖨𝖲 𝖸𝖮𝖴𝖱 {ty} 𝖲𝖳𝖱𝖨𝖭𝖦 𝖲𝖤𝖲𝖲𝖨𝖮𝖭 ❳** \n\n`{string_session}` \n\n**❲ هذا هو كود التيرمكس الخاص بك لا تعطيه لأي شخص لان معرض للختراق :** @Drago_dr ❳"
    try:
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(msg.chat.id, "❲ 𝖲𝖴𝖢𝖢𝖤𝖲𝖲𝖥𝖴𝖫𝖫𝖸 𝖦𝖤𝖭𝖤𝖱 𝖸𝖮𝖴 {} 𝖲𝖳𝖱𝖨𝖭𝖦 𝖲𝖤𝖲𝖲𝖨𝖮𝖭.\n\n𝖯𝖫𝖤𝖠𝖲𝖤 𝖢𝖧𝖤𝖢𝖪 𝖸𝖮𝖴𝖱 𝖲𝖠𝖵𝖤𝖣 𝖬𝖤𝖲𝖲𝖠𝖦𝖤𝖲 𝖳𝖮 𝖦𝖤𝖳 𝖨𝖳 \n\n𝖠 𝖲𝖳𝖱𝖨𝖭𝖦 𝖦𝖤𝖭𝖤𝖱𝖠𝖳𝖮𝖱 𝖡𝖮𝖳 𝖡𝖸︙ @Drago_dr ❳".format("ᴛᴇʟᴇᴛʜᴏɴ" if telethon else "ᴩʏʀᴏɢʀᴀᴍ"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("**» ᴄᴀɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ᴏɴɢᴏɪɴɢs !**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("**❲ 𝖲𝖴𝖢𝖢𝖤𝖲𝖲𝖥𝖴𝖫𝖫𝖸 𝖱𝖤𝖲𝖳𝖠𝖱𝖤𝖣 𝖳𝖧𝖨𝖲 𝖡𝖮𝖳 𝖥𝖮𝖱 𝖸𝖮𝖴 ❳**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/skip" in msg.text:
        return False
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("**❲ 𝖢𝖠𝖭𝖢𝖤𝖫𝖫𝖤𝖣 𝖳𝖧𝖤 𝖮𝖭𝖦𝖮𝖨𝖭𝖦 𝖲𝖳𝖱𝖨𝖭𝖦 𝖦𝖤𝖭𝖱𝖠𝖳𝖨𝖮𝖭 𝖯𝖱𝖮𝖢𝖤𝖲𝖲 ❳**", quote=True)
        return True
    else:
        return False
