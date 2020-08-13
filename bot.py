import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from config import token
import json
PORT = int(os.environ.get('PORT', 5000))

# File Downloads Directory
def create_dir():
    file_downloads_dir = os.path.isdir('./dist')
    if file_downloads_dir == False:
        os.mkdir('./dist')
        print("Directory created!")
        return
    print("Dir already exists!")
    return

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = token

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    jsonFile = json.dumps(update.message.text)
    with open('./dist/file.json', 'wb') as f:
        f.write(jsonFile.encode('utf-8'))
    update.message.reply_text(os.listdir())
    update.message.reply_text('./dist/file.json')
    return  

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    create_dir()
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    # updater.start_webhook(listen="0.0.0.0",
    #                       port=int(PORT),
    #                       url_path=TOKEN)
    # updater.bot.setWebhook('http://localhost:9000/bot/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # updater.start_polling() #is non-blocking and will stop the bot gracefully.
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://webtmblog-bot-01.herokuapp.com/' + TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()