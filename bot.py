import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import MessageEntity
import os
import json
import whois
import datetime
import time
#pttest scrape date of examination
import re
import requests as r
#pttest end

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

#Pttest scrape
def pttest_scrape():
    pattern = "[a-zA-Z]+\s+\d{1,2}[-]\d{1,2}[,]\s+\d{2,4}"
    URL = "https://pttest.icai.org/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    response = r.get(URL, headers=headers).text
    findDate = re.findall(pattern, response)
    return findDate[0]

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = os.getenv("TOKEN")

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text("Hi")
    return

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('1. /pttest for ICAI examination.\n 2. Provide full domain to check domain expiry date.\n')
    
def pttest(update, context):
    """Send a message when the command /pttest is issued."""
    temp = pttest_scrape()
    text = "The date of next examination of ICAI Pttest is {}".format(temp)
    update.message.reply_text(text)

def domain_expiration_date(update, context):
    def myconverter(o):
        if isinstance(o, datetime.datetime):
            return o.__str__()

    domain = update.message.parse_entities(types = MessageEntity.URL)
    for link in domain:
        # print(domain[link])
        try:
            time.sleep(2)
            foo = whois.whois(domain[link])
            result = json.dumps(foo['expiration_date'], default = myconverter)
            update.message.reply_text(result)
        except:
            update.message.reply_text('''You have either provided a wrong URL or We have encountred a server problem.
                \nOr the domain got expired
                \nPlease try again after sometimes!''')

def echo(update, context):
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    # create_dir()
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
    dp.add_handler(CommandHandler("pttest", pttest))

    # log all errors
    dp.add_error_handler(error)

    # domain expiration date command
    dp.add_handler(MessageHandler(Filters.entity(MessageEntity.URL), domain_expiration_date))

    # if no command has been provided then return echo
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Start the Bot
    # updater.start_webhook(listen="0.0.0.0",
    #                       port=int(PORT),
    #                       url_path=TOKEN)
    # updater.bot.setWebhook('http://localhost:9000/bot/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    #updater.start_polling() #is non-blocking and will stop the bot gracefully.
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://webtmblog-bot-01.herokuapp.com/' + TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()