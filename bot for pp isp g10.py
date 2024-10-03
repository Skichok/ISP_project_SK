import math
import telegram
#import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image
import io
import os
from datetime import datetime
import qrcode

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    unique_timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    file_name = f"User_data/{user_id}.txt"

    # Check if the file exists
    if os.path.exists(file_name):
    # If file exists, append the new numbers to a new line
        with open(file_name, 'a') as file:
            file.write(f"\n[{current_time}] {user_id}: /start")
        print(f"Logs added to {file_name}.")
    else:
    # If file doesn't exist, create the file and write the numbers
        with open(file_name, 'w') as file:
            file.write(f"[{current_time}] {user_id}: /start")
        print(f"File {file_name} created and logs saved.")
        
    await update.message.reply_text(f'Hello {update.effective_user.first_name}!\nI am a smart chat-bot!\nList of commands: /list')

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    unique_timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    file_name = f"User_data/{user_id}.txt"

    # Check if the file exists
    if os.path.exists(file_name):
    # If file exists, append the new numbers to a new line
        with open(file_name, 'a') as file:
            file.write(f"\n[{current_time}] {user_id}: /start")
        print(f"Logs added to {file_name}.")
    else:
    # If file doesn't exist, create the file and write the numbers
        with open(file_name, 'w') as file:
            file.write(f"[{current_time}] {user_id}: /hello")
        print(f"File {file_name} created and logs saved.")
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    unique_timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    file_name = f"User_data/{user_id}.txt"

    # Check if the file exists
    if os.path.exists(file_name):
    # If file exists, append the new numbers to a new line
        with open(file_name, 'a') as file:
            file.write(f"\n[{current_time}] {user_id}: /ping")
        print(f"Logs added to {file_name}.")
    else:
    # If file doesn't exist, create the file and write the numbers
        with open(file_name, 'w') as file:
            file.write(f"[{current_time}] {user_id}: /ping")
        print(f"File {file_name} created and logs saved.")
        
    await update.message.reply_text('pong')

async def list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    unique_timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    file_name = f"User_data/{user_id}.txt"

    # Check if the file exists
    if os.path.exists(file_name):
    # If file exists, append the new numbers to a new line
        with open(file_name, 'a') as file:
            file.write(f"\n[{current_time}] {user_id}: /list")
        print(f"Logs added to {file_name}.")
    else:
    # If file doesn't exist, create the file and write the numbers
        with open(file_name, 'w') as file:
            file.write(f"[{current_time}] {user_id}: /list")
        print(f"File {file_name} created and logs saved.")
        
    await update.message.reply_text('Of course, here is the list of commands:\n/start - starts the bot\n/list - list of commands\n/hello - The bot responds with hello and your name in Telegram\n/ping - The bot responds pong\n/buttons - you will get a buttons\n/qrcode [prompt] - Sends back to you QR code for yours prompt\nOr you can send me picture, and I will reply what size it has in pixels!')

async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("Start")
    user_id = update.effective_user.id
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    unique_timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    file_name = f"User_data/{user_id}.txt"

    # Check if the file exists
    if os.path.exists(file_name):
    # If file exists, append the new numbers to a new line
        with open(file_name, 'a') as file:
            file.write(f"\n[{current_time}] {user_id} sent a photo file_{user_id}_{unique_timestamp}")
        print(f"Logs added to {file_name}.")
    else:
    # If file doesn't exist, create the file and write the numbers
        with open(file_name, 'w') as file:
            file.write(f"[{current_time}] {user_id} sent a photo file_{user_id}_{unique_timestamp}")
        print(f"File {file_name} created and logs saved.")
    
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

    file_name = f"User_photo/file_{user_id}_{unique_timestamp}.jpg"  # Unique filename based on file_id
    image.save(file_name)

    # Send the dimensions back to the user
    await update.message.reply_text(f'The photo size is {width}x{height} pixels.')

async def qr_code(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    unique_timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    file_name = f"User_data/{user_id}.txt"
    user_prompt = (update.message.text)[8:]

    # Check if the file exists
    if os.path.exists(file_name):
    # If file exists, append the new numbers to a new line
        with open(file_name, 'a') as file:
            file.write(f"\n[{current_time}] {user_id}: /qrcode {user_prompt} [USER GOT qr_{user_id}_{unique_timestamp}.png]")
        print(f"Logs added to {file_name}.")
    else:
    # If file doesn't exist, create the file and write the numbers
        with open(file_name, 'w') as file:
            file.write(f"[{current_time}] {user_id}: /qrcode {user_prompt} [USER GOT qr_{user_id}_{unique_timestamp}.png]")
        print(f"File {file_name} created and logs saved.")


    img_usr = qrcode.make(user_prompt)  

    type(img_usr)  # qrcode.image.pil.PilImage
    img_usr.save(f"QR_image/qr_{user_id}_{unique_timestamp}.png")
    img_byte_arr = io.BytesIO()
    img_usr.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)  # Go to the start of the BytesIO object
    
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=img_byte_arr)

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_name = f"User_data/{user_id}.txt"

    # Log the command usage
    if os.path.exists(file_name):
        with open(file_name, 'a') as file:
            file.write(f"\n[{current_time}] {user_id}: /buttons")
            print(f"Logs added to {file_name}.")
    else:
        with open(file_name, 'w') as file:
            file.write(f"[{current_time}] {user_id}: /buttons")
            print(f"Logs added to {file_name}.")

    # Create buttons
    keyboard = [
        [InlineKeyboardButton("Button 1", callback_data='button1')],
        [InlineKeyboardButton("Button 2", callback_data='button2')],
        [InlineKeyboardButton("Button 3", callback_data='button3')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send message with inline buttons
    await update.message.reply_text('Choose an option:', reply_markup=reply_markup)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
#    await query.answer()  #approvment of button

    #input check
    if query.data == 'button1':
        user_id = update.effective_user.id
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"User_data/{user_id}.txt"
        if os.path.exists(file_name):
            with open(file_name, 'a') as file:
                file.write(f"\n[{current_time}] {user_id} used button 1")
            print(f"Logs added to {file_name}.")
        else:
            with open(file_name, 'w') as file:
                file.write(f"[{current_time}] {user_id} used button 1")
            print(f"Logs added to {file_name}.")
            
        await query.edit_message_text(text="You pressed button 1!")
        
    elif query.data == 'button2':
        user_id = update.effective_user.id
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"User_data/{user_id}.txt"
        if os.path.exists(file_name):
            with open(file_name, 'a') as file:
                file.write(f"\n[{current_time}] {user_id} used button 2")
            print(f"Logs added to {file_name}.")
        else:
            with open(file_name, 'w') as file:
                file.write(f"[{current_time}] {user_id} used button 2")
            print(f"Logs added to {file_name}.")
            
        await query.edit_message_text(text="You pressed button 2!")
        
    elif query.data == 'button3':
        user_id = update.effective_user.id
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"User_data/{user_id}.txt"
        if os.path.exists(file_name):
            with open(file_name, 'a') as file:
                file.write(f"\n[{current_time}] {user_id} used button 3")
            print(f"Logs added to {file_name}.")
        else:
            with open(file_name, 'w') as file:
                file.write(f"[{current_time}] {user_id} used button 3")
            print(f"Logs added to {file_name}.")
            
        await query.edit_message_text(text="You pressed button 3!")



app = ApplicationBuilder().token("7332049578:AAE5V5jZbLgfPXiLzJoyqZ8cXViNmi3Y0Sk").build()

app.add_handler(CommandHandler("hello", hello))

app.add_handler(CommandHandler("ping", ping))

app.add_handler(CommandHandler("start", start))

app.add_handler(CommandHandler("list", list))

app.add_handler(MessageHandler(filters.PHOTO, photo_handler))

app.add_handler(CommandHandler("qrcode", qr_code))

app.add_handler(CommandHandler("buttons", buttons))

app.add_handler(CallbackQueryHandler(button_callback))

app.run_polling()

#:)
