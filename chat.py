from telegram.ext import (Updater,InlineQueryHandler,CommandHandler, MessageHandler, Filters)
import requests
import re

def get_url(s):
    if s == 'a': 
        contents = requests.get('http://random.dog/woof.json').json()
        url = contents['url']
    elif s == 'b':
        contents = requests.get('https://some-random-api.ml/img/cat').json()
        url = contents['link']
    
    elif s == 'c':
        contents = requests.get('https://some-random-api.ml/img/birb').json()
        url = contents['link']
    
    return url


def woof(bot,update):
    url = get_url('a')
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def meow(bot,update):
    url = get_url('b')
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def birdie(bot,update):
    url = get_url('c')
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def start(bot,update):
    mess = 'Type\n/woof for a dog pic\n/meow for a cat pic\n/birdie for a bird pic'
    bot.send_message(chat_id=update.effective_chat.id, text=mess)
    

def main():
    print('This bot dispenses images\n /woof for a dog image\n /meow for a cat image\n /birdie for a bird image')
    updater = Updater('1226224829:AAGK-3rL1J-O-kYLZkRjzkleZC-aWMZujEc')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('woof',woof))
    dp.add_handler(CommandHandler('birdie',birdie))
    dp.add_handler(CommandHandler('meow',meow))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


