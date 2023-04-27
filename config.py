import os

BOT_API = 'API from Bot Father'

# Webhook configuration
APP_HOST = '0.0.0.0'  # Default value
APP_PORT = '8444'  # Default value
APP_NAME = 'Your-bot-here.herokuapp.com'
WEB_HOOK_URL = f'https://{APP_NAME}/{BOT_API}'

# Database configuration
DB_USERNAME = 'Your value here'
DB_PASSWORD = 'Your value here'
HOST_NAME = 'Your value here'
DB_NAME = 'Your value here'

DB_PORT = '3306'

KEY = 'you-will-never-guess'
basedir = os.path.abspath(os.path.dirname(__file__))


DATABASE_URI = 'mysql://' + f'{DB_USERNAME}:{DB_PASSWORD}@{HOST_NAME}:{DB_PORT}/{DB_NAME}'

# test db
# DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'main.db')

# app config
DEBUG = False  # set True if you want to run it on your pc
NOTIFICATIONS = False  # Requires pro account on the hosting


# class Config(object):
#     SECRET_KEY = os.environ.get('SECRET_KEY') or KEY

