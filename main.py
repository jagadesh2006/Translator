from gtts import gTTS
from googletrans import Translator
import pyrogram 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api_id = 6212815
api_hash = "54ce72519b49dc6d75d3d2b2d6a8f645"
bot_token = "6223458591:AAGc_UAxkJFLboY_NW72nIpr0oQVd-jrV6A"

app = Client("my_bot", api_hash= api_hash, api_id = api_id, bot_token = bot_token)

@app.on_message(filters.text & filters.private)
async def repeat(client,message):
            tts = gTTS(message.text)
            tr_text = translator.translate(message.text,dest = "ja")
            tts.save('text.mp3')
            await message.reply_audio("text.mp3",quote = True)
            await message.reply_text(tr_text.text+"\nPronunciation : "+ tr_text.pronunciation,quote=True,disable_web_page_preview = False)
            tts = gTTS(tr_text.text, lang = "ja")
            tts.save("tr_text.mp3")
            await message.reply_audio("tr_text.mp3",quote = True)
 
 
@app.on_message(filters.command("start"), group =-1)
async def start(client, message):
           await message.reply_text("Hello {} !\nCheck out /help for more help".format(message.chat.first_name))
  
           
                    
START_BUTTONS = InlineKeyboardMarkup(
        [[]
        InlineKeyboardButton('Tutorial 📺', url='https://telegram.me/Deccan_Supportz')
        ]])                             
                                               
@app.on_message(filters.command("help"), group =-1)
async def start(client, message):
           await message.reply("Hello {} !\nJust send me a text .I will translate it for you".format(message.chat.first_name),
           reply_markup=START_BUTTONS
           
           )  
          
app.run()
