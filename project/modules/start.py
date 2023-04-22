from project import bot
from telebot import types
from project.text.text import welcome_message
from project.modules.menu import handle_menu


def handle_start(message: types.Message):
    bot.send_message(message.chat.id, f"Hello, {message.from_user.username}!\n {welcome_message}")
    handle_menu(message)
