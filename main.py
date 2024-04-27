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
        InlineKeyboardButton("Japanese",callback_data ="ja"),
        InlineKeyboardButton("Telugu",callback_data = "te")
    ],[
    	InlineKeyboardButton("✖️ Close",callback_data = "close")
    ]]
)

audio_buttons = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton(" 🎵 Audio",callback_data = "audio"),
        InlineKeyboardButton("🎵 Translated Audio",callback_data ="tr_audio")
    ],[
    	InlineKeyboardButton("🔙 Back",callback_data = "lang"),
    	InlineKeyboardButton("✖️ Close",callback_data = "close")
    ]]
)

close_buttons = InlineKeyboardMarkup(
	[[
		InlineKeyboardButton("✖️ Close",callback_data = "close")
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
        quote= True,
        reply_markup = lang_buttons,
        )
  
@app.on_callback_query(filters.regex("lang"))
async def lang(Client,message):
    await message.edit_message_text(
        "Choose Below Language to translate the text..",
        reply_markup = lang_buttons,)
    print(message)

@app.on_callback_query(filters.regex("close"))
async def close(client,message):
      await message.message.delete()
        		
@app.on_callback_query(filters.regex("tr_audio"))
async def tr_audio(client,message):
	print(message)
	tts = gTTS(tr_text.text,lang=language)
	tts.save("tr_audio.mp3")
	await message.message.reply_audio("tr_audio.mp3")     

@app.on_callback_query(filters.regex("audio"))
async def audio(client,message):
	text = message.message.reply_to_message.text
	tts = gTTS(text)
	tts.save("audio.mp3")
	await message.message.reply_audio("audio.mp3", reply_markup = close_buttons)     
	   
@app.on_callback_query()
async def translate(Client,message):
    global language
    language = message.data
    global tr_text
    tr_text = translator.translate(message.message.reply_to_message.text,dest = language)
    await message.edit_message_text(tr_text.text +"\nPronunciation :"+ tr_text.pronunciation,
       reply_markup = audio_buttons
   )
                        

app.run()
