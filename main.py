from gtts import gTTS
import googletrans
from googletrans import Translator
import pyrogram 
from pyrogram import Client, filters,enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from lang_list import langs
import os


api_id = 6212815
api_hash = "54ce72519b49dc6d75d3d2b2d6a8f645"
bot_token = "7119488856:AAGoBMkOuIyISjVpdTV-naAK5l4I1lJ07tE"

app = Client("my_bot", api_hash= api_hash, api_id = api_id, bot_token = bot_token,port = 0.0.0.0)
translator = Translator()
language = None

donate_text = "Thank you for clicking donate Button."

start_text = """
Hey **{}!**
I am Translator Robot.Just send me a Text to Translate..
Click Help to know more..

**©️ @Deccan_Botz**
"""

help_text = """
Hey **{}!**.
Follow these steps for 
**Translation :**
➖️ Send/Forward me a text to Translate.
➖️ Choose a language from the given languages to translate

**🎵 Audio :**
➖️ Choose **Audio** to get the speech of your text.
➖️ Choose **Translated Audio** to get the speech of translated audio with translated language slang.

**✖️ Close :**
You can close the any active message with close button.

**🔙 Back :**
You can click on Back button to choose other languages and get the translated text and audio for any active message.

**🛠 Updates :**
Send /updates or Updates Button to get future updates.

**💰 Donate :**
It is optional.If you like to donate,then you can send /donate or click on donate button.

**©️ @Deccan_Botz**
"""
updates_text ="""
**Upcoming Features:**
Fix and Unfix a language for Translation.

Request a Feature in **Support Group**

**©️ @Deccan_Botz**
"""
donate_link = "https://paytm.com"

start_buttons = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton("🔧 Help",callback_data = "help"),
        InlineKeyboardButton("✖️ Close",callback_data = "close")
    ]]
)
help_buttons = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton("📢 Channel ",url = "https://t.me/Deccan_Botz"),
        InlineKeyboardButton("🛠 Updates",callback_data = "updates")
        ],
        [
        InlineKeyboardButton("💰 Donate",callback_data = "donate"),
        InlineKeyboardButton("✖️ Close",callback_data = "close")
    ]]
)

lang_buttons = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton("Albanian", callback_data='sq'),
        InlineKeyboardButton("Arabic", callback_data='ar'),
        InlineKeyboardButton("Belarusian",callback_data='be')
        ],
        [
        InlineKeyboardButton("Bengali", callback_data='bn'),
        InlineKeyboardButton("Bulgarian", callback_data='bg'),
        InlineKeyboardButton("Chinese",callback_data= 'zh-cn')
        ],
        [
        InlineKeyboardButton("Czech", callback_data='cs'),
        InlineKeyboardButton("Dutch", callback_data='nl'),
        InlineKeyboardButton("English", callback_data='en')
        ],
        [
        InlineKeyboardButton("Esperanto", callback_data='eo'),
        InlineKeyboardButton("Filipino", callback_data='tl'),
        InlineKeyboardButton("French", callback_data='fr')
        ],
        [InlineKeyboardButton("Georgian", callback_data='ka'),
         InlineKeyboardButton("German", callback_data='de'),
         InlineKeyboardButton("Greek", callback_data='el')
        ],
        [InlineKeyboardButton("Gujarati", callback_data='gu'),
         InlineKeyboardButton("Hawaiian", callback_data='haw'),
         InlineKeyboardButton("Hindi", callback_data='hi')
        ],
        [InlineKeyboardButton("Indonesian", callback_data='id'),
         InlineKeyboardButton("Italian", callback_data='it'),
         InlineKeyboardButton("Japanese", callback_data='ja')
        ],
        [InlineKeyboardButton("Kannada", callback_data='kn'),
         InlineKeyboardButton("Kazakh", callback_data='kk'),
         InlineKeyboardButton("Korean", callback_data='ko')
        ],
        [
          InlineKeyboardButton("🔜 Next",callback_data = "lang1"),
    	     InlineKeyboardButton("✖️ Close",callback_data = "close")
    ]]
)

lang1_buttons = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton("Kurdish", callback_data='ku'),
        InlineKeyboardButton("Latin", callback_data='la'),
        InlineKeyboardButton("Luxembourgish",callback_data='lb')
        ],
        [
        InlineKeyboardButton("Malayalam", callback_data='ml'),
        InlineKeyboardButton("Marathi", callback_data='mr'),
        InlineKeyboardButton("Mongolian",callback_data= 'mn')
        ],
        [
        InlineKeyboardButton("Myanmar", callback_data='my'),
        InlineKeyboardButton("Nepali", callback_data='ne'),
        InlineKeyboardButton("Odia", callback_data='en')
        ],
        [
        InlineKeyboardButton("Persian", callback_data='fa'),
        InlineKeyboardButton("Polish", callback_data='po'),
        InlineKeyboardButton("Portuguese", callback_data='pt')
        ],
        [InlineKeyboardButton("Punjabi", callback_data='pa'),
         InlineKeyboardButton("Romanian", callback_data='ro'),
         InlineKeyboardButton("Russian", callback_data='ru')
        ],
        [InlineKeyboardButton("Serbian", callback_data='sr'),
         InlineKeyboardButton("Sinhala", callback_data='si'),
         InlineKeyboardButton("Spanish", callback_data='es'),
        ],
        [InlineKeyboardButton("Tamil", callback_data='ta'),
         InlineKeyboardButton("Telugu", callback_data='te'),
         InlineKeyboardButton("Thai", callback_data='th')
        ],
        [InlineKeyboardButton("Ukrainian", callback_data='uk'),
         InlineKeyboardButton("Urdu", callback_data='ur'),
         InlineKeyboardButton("Vietnamese", callback_data='vi')
        ],
    [
        InlineKeyboardButton("🔙 Previous",callback_data = "lang"),
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

donate_button = InlineKeyboardMarkup(
     [[
          InlineKeyboardButton("💰 Donate",callback_data="donate"),
          InlineKeyboardButton("✖️ Close",callback_data = "close")

     ]]
)

updates_buttons = InlineKeyboardMarkup(
     [[
          InlineKeyboardButton("📢 Channel ",url = "https://t.me/Deccan_Botz"),
          InlineKeyboardButton("🔧 Help",callback_data = "help")
     ],
     [
     	InlineKeyboardButton("📞 Group",url = "https://t.me/Deccan_Supportz"),
          InlineKeyboardButton("✖️ Close",callback_data = "close")
     ]]
)
error_buttons = InlineKeyboardMarkup(
     [
     [
     	InlineKeyboardButton("📞 Report",url = "https://t.me/Deccan_Supportz"),
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
@app.on_message(filters.command("help"))
async def help(Client,message):
     await message.reply(
          help_text.format(message.chat.first_name),
          reply_markup = help_buttons
     )
@app.on_message(filters.command("updates"))
async def updates(Client,message):
     await message.reply(
          updates_text,
          reply_markup = updates_buttons
     )
@app.on_message(filters.command("donate"))
async def updates(Client,message):
     await message.reply_photo("https://telegra.ph/file/97186d48e986c5d65bb45.jpg",caption = "Scan this QR Code to Donate.",reply_markup = close_buttons
     )

@app.on_message(filters.private & filters.text)
async def lang(Client,message):
    await message.reply(
        "Choose Below Language to translate the text..",
        quote= True,
        reply_markup = lang_buttons,
        )

@app.on_callback_query(filters.regex("set_lang"))
async def set_lang(Client,message):
     await message.edit_message_text("Choose Below to set a Language", reply_markup = lang_buttons)
     print(language)
     @app.on_callback_query()
     async def set_lang1(Client,message):
          language = message.data
          print(language)
          
@app.on_callback_query(filters.regex("lang1"))
async def lang(Client,message):
    await message.edit_message_text(
        "Choose Below Language to translate the text..",
        reply_markup = lang1_buttons)
        
@app.on_callback_query(filters.regex("lang"))
async def lang(Client,message):
    await message.edit_message_text(
        "Choose Below Language to translate the text..",
        reply_markup = lang_buttons)

@app.on_callback_query(filters.regex("close"))
async def close(client,message):
      await message.message.delete()

@app.on_callback_query(filters.regex("help"))
async def help(Client,message):
     await message.edit_message_text(help_text.format(message.message.chat.first_name),reply_markup = help_buttons)

@app.on_callback_query(filters.regex("donate"))
async def donate(Client,message):
     await message.message.reply_photo("https://telegra.ph/file/97186d48e986c5d65bb45.jpg",caption = "Scan this QR Code to Donate.",reply_markup = close_buttons
     )
     
@app.on_callback_query(filters.regex("updates"))
async def donate(Client,message):
     await message.edit_message_text(updates_text,reply_markup = updates_buttons)
        		
@app.on_callback_query(filters.regex("tr_audio"))
async def tr_audio(client,message):
     try:
          tts = gTTS(tr_text.text,lang=language)
          tts.save("tr_audio.mp3")
          await message.message.reply_audio("tr_audio.mp3",reply_markup = donate_button)
     except Exception as e:
            await message.message.reply_text(f"Error : {e}",reply_markup=error_buttons)

@app.on_callback_query(filters.regex("audio"))
async def audio(client,message):
	text = message.message.reply_to_message.text
	tts = gTTS(text)
	tts.save("audio.mp3")
	await message.message.reply_audio("audio.mp3", reply_markup = close_buttons)     
	   
@app.on_callback_query()
async def translate(Client,message):
     try:
          global language
          language = message.data
          global tr_text
          tr_text = translator.translate(message.message.reply_to_message.text,dest = language)
          text = message.message.reply_to_message.text
          src = translator.detect(text).lang
          for lang in langs:
          	if langs[lang] == src:
          		src = lang.capitalize()
          if tr_text.pronunciation != None:
                await message.edit_message_text("``"+tr_text.text +"``"+"\n**Pronunciation :**"+ tr_text.pronunciation+ "\nDetected Language : "+"**"+src+"**",reply_markup = audio_buttons)
          else:
               await message.edit_message_text("``"+tr_text.text +"``"+ "\nDetected Language : "+"**"+src+"**",reply_markup = audio_buttons)
     except Exception as e:
            await message.edit_message_text(f"Error : {e}",reply_markup=error_buttons)
            await message.edit_message_text("``"+tr_text.text +"``"+"\n**Pronunciation :**"+ tr_text.pronunciation+ "\nDetected Language : "+"**"+src+"**",reply_markup = audio_buttons)

app.run()
