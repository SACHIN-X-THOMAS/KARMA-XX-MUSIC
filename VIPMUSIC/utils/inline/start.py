from pyrogram.types import InlineKeyboardButton

import config
from VIPMUSIC import app
from config import SUPPORT_CHAT, SUPPORT_CHANNEL, OWNER_ID

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="☢ sᴇᴛᴛɪɴɢ ☢", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="✡ ɢʀᴏᴜᴘ ✡", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons
    
def private_panel(_):
    buttons = [
        [InlineKeyboardButton(
                text= "✚ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ✚",
                url=f"https://t.me/{app.username}?startgroup=true")]
    ]
    if SUPPORT_CHANNEL and SUPPORT_CHAT:
        buttons.append(
            [
                InlineKeyboardButton(text="📨 Cʜᴀɴɴᴇʟ", url=f"{SUPPORT_CHANNEL}"),
                InlineKeyboardButton(text="📨 Sᴜᴘᴘᴏʀᴛ", url=f"{SUPPORT_CHAT}"),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [InlineKeyboardButton(text="📨 Cʜᴀɴɴᴇʟ", url=f"{SUPPORT_CHANNEL}")]
            )
        if SUPPORT_CHAT:
            buttons.append(
                [InlineKeyboardButton(text="📨 Sᴜᴘᴘᴏʀᴛ", url=f"{SUPPORT_CHAT}")]
            )
    buttons.append(
        [
            InlineKeyboardButton(
                text= "✚ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ✚",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ]
    )
    buttons.append(
        [
            InlineKeyboardButton(text="🫧 ᴘʀᴏғᴇssᴏʀ sᴏᴜʀᴀʙʜ🫧", user_id=OWNER_ID),
        ]
    )
    return buttons
