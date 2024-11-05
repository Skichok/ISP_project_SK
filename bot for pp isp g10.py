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
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp  # to parse mathematical expressions
import imageio
import re
from icrawler.builtin import GoogleImageCrawler

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
        
    await update.message.reply_text('Of course, here is the list of commands:\n/start - starts the bot\n/list - list of commands\n/hello - The bot responds with hello and your name in Telegram\n/buttons - you will get a buttons\n/qrcode [prompt] - Sends back to you QR code for yours prompt\n/graph [function] - you can send function and bot will send back graph of this function! (For example: 2x-3, sin(x), x^2)\n/polgraph [function] - you can send function and bot will send back graph of this function! (For example: r, sin(r), abs(r), or if you want a graph of heart: 2-2*sin(r)+sin(r)*(sqrt(abs(cos(r)))/(sin(r)+1.4)))\n/findphoto [prompt] - Will send you a google picture.\n\nOr you can send me picture, and I will reply what size it has in pixels!')

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

async def graph(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    username = update.effective_user.username
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    unique_timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    file_name = f"User_data/{user_id}.txt"

    # Log the command usage
    expression_text = ' '.join(context.args)  # Get the expression from the command arguments

    # Append log entry
    if os.path.exists(file_name):
        with open(file_name, 'a') as file:
            file.write(f"\n[{current_time}] {user_id}: /graph {expression_text}")
        print(f"Logs added to {file_name}.")
    else:
        with open(file_name, 'w') as file:
            file.write(f"[{current_time}] {user_id}: /graph {expression_text}")
        print(f"File {file_name} created and logs saved.")

    # Insert '*' between numbers and variables (e.g., convert '2x' to '2*x')
    expression_text = re.sub(r'(?<=[0-9])(?=[a-zA-Z])', '*', expression_text)

    # Parse the expression
    try:
        x = sp.symbols('x')  # Define the symbol 'x'
        expression = sp.sympify(expression_text)  # Parse the expression
    except (sp.SympifyError, ValueError):
        await update.message.reply_text("Invalid mathematical expression. Please try again.")
        return

    # Generate values for x and evaluate y based on the expression
    x_values = np.linspace(-10, 10, 400)
    try:
        # Use lambdify to convert sympy expression to a function that numpy can understand
        y_values = sp.lambdify(x, expression, "numpy")(x_values)
    except Exception as e:
        await update.message.reply_text("Error evaluating the expression. Please check the function syntax.")
        return

    # Plot the function with a dark theme
    plt.figure(facecolor='black')  # Set the figure background color
    plt.plot(x_values, y_values, color='cyan', label=f'y = {expression_text}')  # Plot in cyan color

    # Add coordinate axes
    plt.axhline(0, color='white', linewidth=0.8)  # x-axis in white
    plt.axvline(0, color='white', linewidth=0.8)  # y-axis in white

    # Title and labels with white color for visibility on dark background
    plt.title(f'Graph of y = {expression_text}', color='white')
    plt.xlabel('x', color='white')
    plt.ylabel('y', color='white')

    # Additional plot formatting
    plt.grid(True, color='gray')  # Set gridlines to gray
    plt.legend(facecolor='black', edgecolor='white', labelcolor='white', loc='upper right')  # Legend with white text
    plt.gca().set_facecolor("black")  # Set the axes background color to black
    plt.tick_params(colors='white')  # Set the tick labels color to white

    # Save the plot with a unique filename
    graph_filename = f"Graph_pic/graph_{username}_{unique_timestamp}.png"
    plt.savefig(graph_filename, facecolor='black')  # Ensure the background remains black when saved
    plt.close()

    # Send the plot back to the user
    with open(graph_filename, 'rb') as image_file:
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_file)

async def polgraph(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    username = update.effective_user.username
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    unique_timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    file_name = f"User_data/{user_id}.txt"

    # Log the command usage
    expression_text = ' '.join(context.args)  # Get the expression from the command arguments

    # Append log entry
    if os.path.exists(file_name):
        with open(file_name, 'a') as file:
            file.write(f"\n[{current_time}] {user_id}: /polgraph {expression_text}")
        print(f"Logs added to {file_name}.")
    else:
        with open(file_name, 'w') as file:
            file.write(f"[{current_time}] {user_id}: /polgraph {expression_text}")
        print(f"File {file_name} created and logs saved.")

    # Insert '*' between numbers and variables for multiplication (e.g., convert '2r' to '2*r')
    expression_text = re.sub(r'(?<=[0-9])(?=[a-zA-Z])', '*', expression_text)

    # Parse the expression
    try:
        r = sp.symbols('r')  # Define the symbol 'r' for polar coordinates
        expression = sp.sympify(expression_text)  # Parse the expression
    except (sp.SympifyError, ValueError):
        await update.message.reply_text("Invalid mathematical expression. Please try again.")
        return

    # Generate theta values
    theta_values = np.linspace(0, 2 * np.pi, 400)  # 0 to 2π
    try:
        # Use lambdify to convert sympy expression to a function that numpy can understand
        r_values = sp.lambdify(r, expression, "numpy")(theta_values)  # Evaluate r as a function of theta
    except Exception as e:
        await update.message.reply_text("Error evaluating the expression. Please check the function syntax.")
        return

    # Create polar plot
    plt.figure(facecolor='black')  # Set the figure background color
    ax = plt.subplot(111, projection='polar')  # Create polar subplot
    ax.plot(theta_values, r_values, color='cyan', label=f'r = {expression_text}')  # Plot in cyan color

    # Title and labels with white color for visibility on dark background
    ax.set_title(f'Polar Graph of r = {expression_text}', color='white')
    ax.set_xlabel('θ', color='white')  # Label for theta
    ax.set_ylabel('r', color='white')  # Label for r

    # Additional plot formatting
    ax.grid(color='gray')  # Set gridlines to gray
    ax.legend(facecolor='black', edgecolor='white', labelcolor='white', loc='upper right')  # Legend with white text
    ax.tick_params(colors='white')  # Set the tick labels color to white
    ax.set_facecolor("black")  # Set the axes background color to black

    # Save the polar plot with a unique filename
    polar_graph_filename = f"PGraph_pic/polar_graph_{username}_{unique_timestamp}.png"
    plt.savefig(polar_graph_filename, facecolor='black')  # Ensure the background remains black when saved
    plt.close()

    # Send the polar plot back to the user
    with open(polar_graph_filename, 'rb') as image_file:
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_file)


async def findphoto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    username = update.effective_user.username
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    datestamp = datetime.now().strftime("%Y%m%d")

    # Log command usage
    file_name = f"User_data/{user_id}.txt"
    if os.path.exists(file_name):
        with open(file_name, 'a') as file:
            file.write(f"\n[{current_time}] {user_id}: /findphoto {context.args} [USER GOT foundphoto_{username}_{datestamp}.jpg]")
    else:
        with open(file_name, 'w') as file:
            file.write(f"[{current_time}] {user_id}: /findphoto {context.args} [USER GOT foundphoto_{username}_{datestamp}.jpg]")

    # Get the search query
    query = ' '.join(context.args)  # Join all arguments as a single search query
    if not query:
        await update.message.reply_text("Please provide a search query after the command.")
        return

    # Create an instance of GoogleImageCrawler
    google_crawler = GoogleImageCrawler(storage={'root_dir': 'G_pic'})

    # Crawl for images using the provided query
    google_crawler.crawl(keyword=query, max_num=1)

    # After crawling, check for the downloaded image and rename it
    original_image_pattern = 'G_pic/000001.jpg'  # Default filename from icrawler
    found_image_filename = f"foundphoto_{username}_{datestamp}.jpg"
    new_image_path = os.path.join('G_pic', found_image_filename)

    # Check if the original image exists and rename it
    if os.path.exists(original_image_pattern):
        # Ensure the new filename is unique
        counter = 1
        unique_new_image_path = new_image_path
        while os.path.exists(unique_new_image_path):
            unique_new_image_path = os.path.join('G_pic', f"foundphoto_{username}_{datestamp}_{counter}.jpg")
            counter += 1

        # Rename the image file
        os.rename(original_image_pattern, unique_new_image_path)

        # Send the found image back to the user
        with open(unique_new_image_path, 'rb') as image_file:
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_file)
    else:
        await update.message.reply_text("No image found for your query.")



app = ApplicationBuilder().token("7332049578:AAE5V5jZbLgfPXiLzJoyqZ8cXViNmi3Y0Sk").build()

app.add_handler(CommandHandler("hello", hello))

app.add_handler(CommandHandler("ping", ping))

app.add_handler(CommandHandler("start", start))

app.add_handler(CommandHandler("list", list))

app.add_handler(MessageHandler(filters.PHOTO, photo_handler))

app.add_handler(CommandHandler("qrcode", qr_code))

app.add_handler(CommandHandler("buttons", buttons))

app.add_handler(CommandHandler("graph", graph))

app.add_handler(CommandHandler("polgraph", polgraph))

app.add_handler(CommandHandler("findphoto", findphoto))

app.add_handler(CallbackQueryHandler(button_callback))

app.run_polling()

#:)
