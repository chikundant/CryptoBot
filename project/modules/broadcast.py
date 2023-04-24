import time
import pycoingecko

import config
from project import session
from project.models import User
from project import bot
from project.modules.coins_menu import get_user_coins
from project.crypto_api_request import cg


# INTERVAL = 3600
INTERVAL = 60


def send_message():
    if config.NOTIFICATIONS is True:
        while True:
            try:
                time.sleep(INTERVAL)
                users = session.query(User).all()
                for user in users:
                    coins = get_user_coins(user.telegram_id)
                    data = cg.get_price(ids=coins, vs_currencies='usd')
                    info = ''
                    for coin in coins:
                        info += f"{coin.upper()} {data[coin]['usd']}\n"
                    bot.send_message(user.telegram_id, info)
            except Exception as e:
                print(e)
                continue
