from pyrogram import filters, Client, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
import random

from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

force_channel = "crazy_cinemas_official"

PICS = [
 "https://telegra.ph/file/f75305e1b49490b793f28.jpg"
]

VID = [
 "https://telegra.ph/file/d5082ef18ad41aa35d074.mp4"
]

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    if force_channel:
        try:
            user = await bot.get_chat_member(force_channel, update.from_user.id)
            if user.status == "kicked out":
                await update.reply_text("You Are Banned")
                return
        except UserNotParticipant :
            await update.reply_photo(
                photo=random.choice(PICS),
                caption="🔊 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗠𝗮𝗶𝗻 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 🤭.\n\nനിങ്ങൾക്ക് മൂവീസ് വേണോ? എങ്കിൽ തായെ കാണുന്ന ഞങ്ങളുടെ മെയിൻ ചാനലിൽ ജോയിൻ ചെയ്യുക.😂\nഎന്നിട്ട് ഗ്രൂപ്പിൽ പോയി വീണ്ടും മൂവിയിൽ ക്ലിക് ചെയ്ത് start കൊടുത്തു നോക്കൂ..!😁",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("🔊 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗠𝗮𝗶𝗻 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 🤭", url=random.choice(force_channel))
                 ]]
                 )
            )
            return
   
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type, file_size = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
     #CUSTOM FILE CAPTION   
        caption=f"""Hey {update.from_user.mention} 😍
        
<code>{file_name} </code>

♻️ 𝙅𝙊𝙄𝙉 :- @CC_LinkzzTG"""
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = caption,
                reply_markup=InlineKeyboardMarkup( [[
                    InlineKeyboardButton("👨‍💻 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋", url="t.me/MR_HKZ_TG"),
                    ],[
                    InlineKeyboardButton("𝖩𝗈𝗂𝗇 𝖿𝗈𝗋 𝖬𝗈𝗏𝗂𝖾𝗌 🌀", url="https://t.me/CCGroupOfficial")
                    ]]
                    )
                )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode=enums.ParseMode.HTML)
            LOGGER(__name__).error(e)
        return
#pmstart
    buttons = [[
                    InlineKeyboardButton("👨‍💻 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋", url="t.me/MR_HKZ_TG")
                ],[
                    InlineKeyboardButton("𝖩𝗈𝗂𝗇 𝖿𝗈𝗋 𝖬𝗈𝗏𝗂𝖾𝗌 🌀", url="https://t.me/CCGroupOfficial")
           ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await update.reply_photo(
        photo=random.choice(PICS),
        caption=Translation.START_TEXT.format(update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup( [[
                    InlineKeyboardButton("𝖠𝖽𝖽 𝗆𝖾 𝗍𝗈 𝗒𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 🎗", url="http://t.me/CCResmiBot?startgroup=true"),
                    ],[
                    InlineKeyboardButton("👨‍💻 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋", url="t.me/MR_HKZ_TG"),
                    InlineKeyboardButton("𝖩𝗈𝗂𝗇 𝖿𝗈𝗋 𝖬𝗈𝗏𝗂𝖾𝗌 🌀", url="https://t.me/CCGroupOfficial")
                    ]]
                    )
   )
     
     
     
