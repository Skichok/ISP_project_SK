import math
import telegram
#import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from PIL import Image
import io

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}!\nI am a chat bot that can analyze websites and also send your prompt to Google`s Gemini neural network.\nList of commands: /list')
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('pong')

async def list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Of course, here is the list of commands:\n/start - starts the bot\n/list - list of commands\n/hello - The bot responds with hello and your name in Telegram\n/ping - The bot responds pong\n/start')

async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("Start")
    # Get the photo file (use the largest available size)
    photo = update.message.photo[-1]
    print(0)
    file = await photo.get_file()
    print(1)
    
    # Download the photo
    photo_data = await file.download_as_bytearray()

    # Load the image using PIL
    image = Image.open(io.BytesIO(photo_data))
    width, height = image.size

    # Send the dimensions back to the user
    await update.message.reply_text(f'The photo size is {width}x{height} pixels.')


app = ApplicationBuilder().token("7332049578:AAE5V5jZbLgfPXiLzJoyqZ8cXViNmi3Y0Sk").build()

app.add_handler(CommandHandler("hello", hello))

app.add_handler(CommandHandler("ping", ping))

app.add_handler(CommandHandler("start", start))

app.add_handler(CommandHandler("list", list))

app.add_handler(MessageHandler(filters.PHOTO, photo_handler))

app.run_polling()

#:)
