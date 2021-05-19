from pyrogram import Client
from sample_config import Config
from plugins.help_text import rename_cb, cancel_extract
from plugins.rename_file import force_name


@Client.on_callback_query()
async def cb_handler(bot, update):
        
    if "rename_button" in update.data:
        await update.message.delete()
        await force_name(bot, update.message)     
    elif "cancel_e" in update.data:
        await update.message.delete()
        await cancel_extract(bot, update.message)
    elif "chnl1" in update.data:
        await update.msg.copy_message(
            chat_id=Config.CHANNEL_ID_1
        )
 
