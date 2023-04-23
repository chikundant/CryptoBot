from project import bot
from telebot import types
from project.modules import start
import project.modules.registration as registration


@bot.message_handler(commands=['start'])
@registration.restricted_access
def start_handler(message: types.Message):
    start.handle_start(message)

#
# @bot.message_handler(commands=['register'])
# def menu_handler(message: types.Message):
#     registration.registration(message)


