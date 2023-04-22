from project import bot
from telebot import types


def handle_menu(message: types.Message):
    bot.send_message(message.chat.id, f"Hello, {message.from_user.username}!")
