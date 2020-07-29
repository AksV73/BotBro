from telegram.ext import Updater,InlineQueryHandler, CommandHandler
import requests
import re

def get_url():
    contents = requests.get('http://random.dog/woof.json').json()
    url = contents['url']
    return url

def bop(bot,update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('Telegram-bot-token')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


