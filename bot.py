import logging
import os
import telegram
from urllib import request
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters


logging.basicConfig(
    level = logging.INFO,format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s,"
)

logger = logging.getLogger()
TOKEN = '5077143516:AAElprNXPadSVu3I_57KlGthNAaLRzyoyzc' # aki cambia esto por el token que te da botfather

if name == '__main__':
    my_bot = telegram.Bot(token = TOKEN)


def recv(update,context):
    CHAT_ID = update.message.chat.id
    context.bot.sendMessage(chat_id = CHAT_ID,text = '' + update.message.text + '',parse_mode = 'MarkdownV2')


updater = Updater(my_bot.token,use_context = True);
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text,recv))
updater.start_polling()

updater.idle()
