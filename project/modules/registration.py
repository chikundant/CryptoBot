from project import bot, session
from telebot import types
from project.models import User
import project.modules.menu as menu
import project.modules.coins_menu as coins_menu
from sqlalchemy.exc import IntegrityError
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


def restricted_access(func):
    def wrapper(message):
        if session.query(User).filter_by(telegram_id=str(message.from_user.id)).first():
            func(message)
        else:
            registration(message)
    return wrapper


def registration(message: types.Message):
    user = User(telegram_id=message.from_user.id)
    bot.send_message(message.chat.id, "Hello! Please register by sending me your name")
    bot.register_next_step_handler(message, register_name, user)


def register_name(message, user):
    if user.name is None:
        user.name = message.text
        bot.send_message(message.chat.id, "Got it! Please send me your email.")

    bot.register_next_step_handler(message, register_email, user)


def register_email(message, user):

    if re.fullmatch(regex, message.text):
        user.email = message.text
        bot.send_message(message.chat.id, "Thanks! Please send me your password.")
        bot.register_next_step_handler(message, register_password, user)
    else:
        bot.send_message(message.chat.id, "Please write correct email!")
        # bot.register_next_step_handler(message, register_email, user)
        register_name(message, user)


def register_password(message, user):
    markup = types.ReplyKeyboardMarkup(True, True)

    button1 = types.KeyboardButton('Yes')
    button2 = types.KeyboardButton('Change')

    markup.row(button1)
    markup.row(button2)

    user.password_hash = message.text
    bot.send_message(message.chat.id, f"Is this information correct?\n\n"
                                      f"{user.name}\n"
                                      f"{user.email}\n"
                                      f"{user.password_hash}\n", reply_markup=markup)

    bot.register_next_step_handler(message, save_user, user)


def save_user(message, user):
    if message.text == 'Yes':
        try:
            user.set_password(user.password_hash)
            session.add(user)
            session.commit()
            coins_menu.init_user_coins(user.telegram_id)
            menu.handle_menu(message)
        except IntegrityError:
            bot.send_message(message.chat.id, f'Seems like you have already registered!')
            menu.handle_menu(message)
    else:
        registration(message)
