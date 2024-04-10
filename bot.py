import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "6965255627:AAGHAspJSX01m1vaKfp6faZdWRJg-hDQtKg"

def start(update, context):
    update.message.reply_text("Welcome to the Zee5 Downloader Bot! Send me the Zee5 video link you want to download.")

def download_zee5_video(update, context):
    zee5_link = update.message.text
    response = requests.get(zee5_link)
    
    # Add code here to extract the video URL from the response
    
    # Add code here to download the video
    
    update.message.reply_text("Video downloaded successfully! 🎥🔥")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, download_zee5_video))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
