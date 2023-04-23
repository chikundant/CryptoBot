from project import bot
from telebot import types
import json
import project.crypto_api_request as crypto_api_request
import project.modules.menu as menu


def init_user_coins(user_id: str, new_coin=None):

    with open('user_coins.json', 'r') as file:
        data = json.loads(file.readline())
        if user_id not in data:
            data[user_id] = crypto_api_request.COINS

    if new_coin is not None:
        coins_list = crypto_api_request.COINS
        data[user_id] = coins_list.append(new_coin)

    data[user_id] = crypto_api_request.COINS
    with open('user_coins.json', 'w') as file:
        json.dump(data, file)


def get_user_coins(user_id):
    with open('user_coins.json', 'r') as file:
        data = json.loads(file.readline())
        return data[str(user_id)]


def add_new_coin_handler(message):
    bot.send_message(message.chat.id, 'Please, text me a coin you want to add')
    bot.register_next_step_handler(message, add_new_coin)


def add_new_coin(message: types.Message):
    if crypto_api_request.is_correct_coin_name(message.text):
        init_user_coins(str(message.from_user.id), message.text)
        bot.send_message(message.chat.id, 'Coin has successfully added!')

    else:
        bot.send_message(message.chat.id, 'We could not find information about the coin(')

    menu.handle_menu(message)


def show_coins(message):
    markup = menu.create_keyboard(get_user_coins(message.from_user.id))
    bot.send_message(message.chat.id, f'Please, choose currency you want to know about below\n', reply_markup=markup)
    bot.register_next_step_handler(message, show_coin_rate)


def show_coin_rate(message: types.Message):
    bot.send_message(message.chat.id, f'{crypto_api_request.get_coin_rate(message.text)}')
    menu.handle_menu(message)

