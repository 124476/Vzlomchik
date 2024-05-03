import asyncio
import time

import winsound

from telegram import ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters
import logging

import pickle

with open('filename.pickle', 'rb') as pk:
    a = pickle.load(pk)

n = a[0]
BOT_TOKEN = a[1]

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def echo(update, context):
    global n
    if update.message.text == '/start':
        n = True
        with open('filename.pickle', 'wb') as pk:
            pickle.dump([True, BOT_TOKEN], pk)
        await update.message.reply_text(f'Запуск')

    elif update.message.text == '/stop':
        n = False
        with open('filename.pickle', 'wb') as pk:
            pickle.dump([False, BOT_TOKEN], pk)

        await update.message.reply_text(f'Остановка')
    elif update.message.text == '/commands':
        reply_keyboard = [['/start', '/stop']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
        await update.message.reply_text(
            "Commands:",
            reply_markup=markup
        )
    else:
        await update.message.reply_text(f'Ошибка')


async def f():
    while True:
        if n:
            winsound.PlaySound('data/agogo-bells__025_mezzo-forte_struck-singly.mp3', winsound.SND_FILENAME)
        await asyncio.sleep(0.1)


loop = asyncio.get_event_loop()
loop.create_task(f())

application = Application.builder().token(BOT_TOKEN).build()
text_handler = MessageHandler(filters.TEXT, echo)
application.add_handler(text_handler)
application.run_polling()
