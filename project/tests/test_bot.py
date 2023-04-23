import telebot
import pytest
from telebot.types import Message, User, Chat
from datetime import datetime
from project.routes import start_handler

test_bot = telebot.TeleBot('6161817888:AAG01yBHx-cCcGluoYUxm_mG7QOXRkqvCVE')


@test_bot.message_handler(commands=["start"])
def start_handler(message):
    test_bot.reply_to(message, "Hello, world!")

