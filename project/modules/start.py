from project import bot
from telebot import types
from project.text.text import welcome_message
import project.modules.menu as menu
import project.modules.registration as registration


def handle_start(message: types.Message):
    bot.send_message(message.chat.id, f"Hello, {message.from_user.username}!\n {welcome_message}")
    menu.handle_menu(message)
