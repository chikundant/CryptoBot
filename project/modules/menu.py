from project import bot
from telebot import types

import project.modules.coins_menu as coins_menu
import project.modules.start as start
import math

MENU = ['Coins', 'Add coin']


def start_command_check(func):  # This decorator requires with keyboard as middle handler to check different commands
    def wrapper(message):
        if message.text == '/start':
            start.handle_start(message)
        else:
            func(message)

    return wrapper


def handle_menu(message: types.Message):
    markup = create_keyboard(MENU)
    bot.send_message(message.chat.id, f'Please, choose function below\n', reply_markup=markup)
    bot.register_next_step_handler(message, menu_handler)


@start_command_check
def menu_handler(message: types.Message):
    if message.text == 'Coins':
        coins_menu.show_coins(message)
    elif message.text == 'Add coin':
        coins_menu.add_new_coin_handler(message)
    else:
        handle_menu(message)


def create_keyboard(items, columns=3):
    keyboard = types.ReplyKeyboardMarkup(row_width=columns, resize_keyboard=True)
    rows = int(math.ceil(len(items) / columns))

    for i in range(rows):
        start = i * columns
        end = (i + 1) * columns
        row_items = items[start:end]
        keyboard.row(*row_items)

    return keyboard
