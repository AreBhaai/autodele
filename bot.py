import asyncio
from os import environ
from pyrogram import Client, filters, idle
import os

API_ID       = int(os.environ.get("API_ID", "23642215"))
API_HASH     = os.environ.get("API_HASH", "7fbd4d621dc44fda39956268bb78f42f")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "6728912571:AAFhBuHfBJz7w8nFDPlEPI-t6Sx68Utx2kY")
SESSION      = os.environ.get("SESSION", "AQFowGcAMkv5NEWXmPPp7dQb9qSb-B6ACbQs5khqrAvA5suyl4BWLeL7jT-V5flL4bR2CP0QhI9w83UjZvgi3nl43g59oCFmfFBrNVdAzsDZKXLouU3216tq5pUL-bW5nz29NiOms19CZQwGE9LH0jYn_T_uirSyAdZmeVriUzKinR6Y2zmU5N4-_yBTJZEvb0aWZqXD0n8FUHGwCGCzdXIR0BKFrts-p67COmrubF-GtXcYDC_I1whyrUzrzgoDIlPLJw5iGrQ9Abr2K7-QlanIYzeg1K_I8WYDU6UuuHJ3vw6-MCdnzSeqdYFWUb2-ouILzLyKez6mXRMp0gAOn92OjmlMEgAAAAGlZupAAA")
TIME         = int(os.environ.get("TIME", 5))
GROUPS       = [int(grp) for grp in os.environ.get("GROUPS", "-1002130385569 -1001860587879 -1001998223606 -1001731538618 -1002125318782 -1002124016839 -1001829721717 -1002118247955").split()]
ADMINS       = [int(usr) for usr in os.environ.get("ADMINS", "6446790411").split()]

START_MSG = "<b>സിനിമയാണെങ്കിൽ ഇവിടെ ചോദിക്കല്ലേ. ഗ്രൂപ്പിൽ ചോദിക്ക് ഒക്കെ ബൈ \n\nGroup link https://t.me/+IJh-LnhpCUQwMjE1 https://t.me/+IJh-LnhpCUQwMjE1 https://t.me/+IJh-LnhpCUQwMjE1</b>"


User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )


Bot = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.id)
    except Exception as e:
       print(e)
       
User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
