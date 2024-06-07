import os
import subprocess
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome! Send me a link to download a video.')

def download_video(update: Update, context: CallbackContext) -> None:
    url = update.message.text
    update.message.reply_text(f'Downloading video from {url}...')
    
    try:
        # Extract directory information from user input or URL
        if 'show' in url:  # Example condition to detect TV shows
            show_name = 'ExampleShow'  # Extract show name from URL or user input
            output_dir = os.path.join(context.bot_data['shows_path'], show_name)
        else:
            output_dir = context.bot_data['movies_path']
            
        os.makedirs(output_dir, exist_ok=True)
        
        # Command to download the video using yt-dlp
        command = ['yt-dlp', '-o', os.path.join(output_dir, '%(title)s.%(ext)s'), url]
        subprocess.run(command, check=True)
        
        update.message.reply_text('Download complete!')
    except Exception as e:
        update.message.reply_text(f'Failed to download video: {e}')

def main(api_token: str, movies_path: str, shows_path: str) -> None:
    bot = Bot(api_token)
    updater = Updater(api_token)

    dispatcher = updater.dispatcher
    dispatcher.bot_data['movies_path'] = movies_path
    dispatcher.bot_data['shows_path'] = shows_path
    
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, download_video))

    updater.start_polling()
    updater.idle()
