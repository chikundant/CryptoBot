from project import bot, session
from telebot import types
from project.models import User


def handle_start(message: types.Message):
    bot.send_message(message.chat.id, "Hello! Please register by sending me your email.")
    user = User(username='username', email='12312321', password_hash='2222')
    session.add(user)
    session.commit()
