from project import bot
from telebot import types

from project.crypto_api_request import coins, create_coins_keyboard, get_coin_rate


def handle_menu(message: types.Message):
    markup = create_coins_keyboard()
    bot.send_message(message.chat.id, f'Please, choose currency you want to know about below\n', reply_markup=markup)
    bot.register_next_step_handler(message, get_currency)


def get_currency(message: types.Message):
    bot.send_message(message.chat.id, f'{get_coin_rate(message.text)}')
    handle_menu(message)
