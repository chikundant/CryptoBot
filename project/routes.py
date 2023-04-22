from project import bot
from telebot import types
from project.modules import registration, menu, start


@bot.message_handler(commands=['start'])
def start_handler(message: types.Message):
    start.handle_start(message)


# @bot.message_handler(commands=['menu'])
# def menu_handler(message: types.Message):
#     registration.handle_start(message)


