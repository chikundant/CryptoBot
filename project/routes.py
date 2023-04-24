import config
from project import bot
from telebot import types
import threading

from project.modules import start
import project.modules.registration as registration
from project.modules.broadcast import send_message

# if config.NOTIFICATIONS:
#     broadcast_thread = threading.Thread(target=send_message)
#     broadcast_thread.start()


@bot.message_handler(commands=['start'])
@registration.restricted_access
def start_handler(message: types.Message):
    start.handle_start(message)

