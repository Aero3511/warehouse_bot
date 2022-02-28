import telegram

import bot_tkn
import sqlite3
from telegram.ext import Updater
import logging
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters


# Инициализация подключения к БД


sql_connection = sqlite3.connect('./db/test.db')
cursor = sql_connection.cursor()
print('DB connected')
cursor.execute('SELECT sqlite_version();')
record = cursor.fetchall()
print(record)


#

updater = Updater(token = bot_tkn.tkn, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update: Update, context: CallbackContext):
    # Сначала нужно узать кто ты
    # Проверить в базе данных валидность оператора
    # Отрисовать 4 кнопки
    context.bot.send_message(chat_id=update.effective_chat.id, text="Укажите номер оператора: ")


def create_operator(update: Update, context: CallbackContext):
    print(update.message.text)

    #cursor.execute('SELECT name FROM users WHERE id = ')
    #cursor.close()

start_handler = CommandHandler('start', start)
mes_handler = MessageHandler(~Filters.command, create_operator)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(mes_handler)

updater.start_polling()