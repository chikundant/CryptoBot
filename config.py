import os

BOT_API = '6239549672:AAGvhZ6rvB7GzqJ8xSJar24kKrMEdOqB1YU'

# Webhook configuration
APP_HOST = '0.0.0.0'  # Default value
APP_PORT = '8444'  # Default value
APP_NAME = 'chikunda.pythonanywhere.com'
WEB_HOOK_URL = f'https://{APP_NAME}/{BOT_API}'

# Database configuration
DB_USERNAME = 'chikunda'
DB_PASSWORD = 'D52292023290'
HOST_NAME = 'chikunda.mysql.pythonanywhere-services.com'
DB_NAME = 'chikunda$default'

PORT = '3306'

KEY = 'you-will-never-guess'
basedir = os.path.abspath(os.path.dirname(__file__))


# DATABASE_URI = 'mysql://' + f'{DB_USERNAME}:{DB_PASSWORD}@{HOST_NAME}:{PORT}/{DB_NAME}'

# test db
DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'main.db')

# app config
DEBUG = True  # set True if you want to run it on your pc
NOTIFICATIONS = False  # Requires pro account on the hosting


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or KEY

