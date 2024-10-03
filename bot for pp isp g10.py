import math
import telegram
#import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}!\nI am a chat bot that can analyze websites and also send your prompt to Google`s Gemini neural network.\nList of commands: /list')
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('pong')

async def list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Of course, here is the list of commands:\n/hello - The bot responds with hello and your name in Telegram\n/ping - The bot responds pong\n/analyze_site - The bot takes 3 strings of websites and gives you information about them.\nInput type: \n/analyze_site {site 1}\n{site 2}\n{site 3}\n/freeprompt - The bot accepts the prompt message and then sends you a neural network response.')


app = ApplicationBuilder().token("7332049578:AAE5V5jZbLgfPXiLzJoyqZ8cXViNmi3Y0Sk").build()

app.add_handler(CommandHandler("hello", hello))

app.add_handler(CommandHandler("ping", ping))

app.add_handler(CommandHandler("start", start))

app.add_handler(CommandHandler("list", list))

app.run_polling()
