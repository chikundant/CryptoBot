import requests
from telebot import types
import math

url = 'https://api.coingecko.com/api/v3/simple/price'
coins = ['bitcoin', 'ethereum', 'binancecoin', 'tether', 'cardano', 'dogecoin', 'xrp', 'polkadot', 'usd-coin',
         'uniswap']


def get_coin_rate(coin):
    try:
        params = {f'ids': coin, 'vs_currencies': 'usd', 'include_24hr_change': 'true'}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        price = data[coin]['usd']
        change = data[coin]['usd_24h_change']
        return f"{coin.capitalize()}: ${price:.2f} (24h change: {change:.2f}%)"
    except requests.exceptions.HTTPError as http_error:
        return f'HTTP error occurred: {http_error}'
    except requests.exceptions.ConnectionError as connection_error:
        return f'Connection error occurred: {connection_error}'
    except requests.exceptions.Timeout as timeout_error:
        return f'Request timed out: {timeout_error}'
    except requests.exceptions.RequestException as request_error:
        return f'An error occurred while making the request: {request_error}'
    except KeyError as key_error:
        return f'Wrong input while making the request: {key_error}'


def create_coins_keyboard(columns=3):
    keyboard = types.ReplyKeyboardMarkup(row_width=columns)
    rows = int(math.ceil(len(coins) / columns))

    for i in range(rows):
        start = i * columns
        end = (i + 1) * columns
        row_items = coins[start:end]
        keyboard.row(*row_items)

    return keyboard
