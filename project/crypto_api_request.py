import requests
import pycoingecko

url = 'https://api.coingecko.com/api/v3/simple/price'
COINS = ['bitcoin', 'ethereum', 'binancecoin', 'tether', 'cardano', 'dogecoin', 'polkadot', 'usd-coin',
         'uniswap']

cg = pycoingecko.CoinGeckoAPI()


def get_coin_rate(coin):
    try:
        data = cg.get_coin_by_id(id=coin, tickers=True)
        price = data['market_data']['current_price']['usd']
        change = data['market_data']['price_change_percentage_24h']
        low_24h = data['market_data']['low_24h']['usd']
        high_24h = data['market_data']['high_24h']['usd']
        return f"{coin.capitalize()}: ${price}\n" \
               f"24h change: {change}%\n\n" \
               f"low_24h: ${low_24h}\n" \
               f"low_24h: ${high_24h}"
    except KeyError as key_error:
        return f'Wrong input while making the request: {key_error}'

    except ValueError as value_error:
        return f'Wrong input while making the request: {value_error}'

    except Exception as e:
        return f'Something went wrong: {e}'


def is_correct_coin_name(coin):
    try:
        data = cg.get_coin_by_id(id=coin, tickers=True)
        return True
    except Exception as e:
        return False
