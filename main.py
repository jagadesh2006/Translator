from gtts import gTTS
from googletrans import Translator
import pyrogram 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api_id = 6212815
api_hash = "54ce72519b49dc6d75d3d2b2d6a8f645"
bot_token = "6223458591:AAGc_UAxkJFLboY_NW72nIpr0oQVd-jrV6A"

app = Client("my_bot", api_hash= api_hash, api_id = api_id, bot_token = bot_token)
translator = Translator()

@app.on_message(filters.private & filters.text)
async def translate(Client,message):
    tr_text = translator.translate(message.text,dest = "ja")
    await message.reply(
        tr_text.text,
        "Pronunciation": tr_text.pronunciation,
        quote = "True"
     )
app.run()
            
    
