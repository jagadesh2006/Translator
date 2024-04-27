from gtts import gTTS
from googletrans import Translator
import pyrogram 
from pyrogram import Client, filters,enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api_id = 6212815
api_hash = "54ce72519b49dc6d75d3d2b2d6a8f645"
bot_token = "6223458591:AAGc_UAxkJFLboY_NW72nIpr0oQVd-jrV6A"

app = Client("my_bot", api_hash= api_hash, api_id = api_id, bot_token = bot_token)
translator = Translator()
language = None
start_text = """Hey {}!\nI am Translator Robot. Check /help for more..."""

start_buttons = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton("Set Lang",callback_data = "set_lang")
    ]]
)

lang_buttons = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton("Tamil",callback_data = "ta"),
        InlineKeyboardButton("Japanese",callback_data ="ja)
    ]]
)

audio_buttons = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton("Audio",callback_data = "Audio"),
        InlineKeyboardButton("Translated Audio",callback_data ="Audio")
    ]]
)
@app.on_message(filters.command("start"))
async def start(Client,message):
    await message.reply(
        start_text.format(message.chat.first_name),
        quote = True,
        reply_markup = start_buttons
    )

@app.on_message(filters.private & filters.text)
async def lang(Client,message):
    await message.reply(
        "Choose Below Language to translate the text..",
        reply_markup = lang_buttons
    )
    
@app.on_callback_query()
async def translate(Client,message):
    language = message.data
    tr_text = translator.translate(message.message.reply_to_message.text,dest = language)
    await message.message.reply(tr_text.text +"\nPronunciation :"+ tr_text.pronunciation,
       reply_markup = audio_buttons
   )
                        

app.run()
