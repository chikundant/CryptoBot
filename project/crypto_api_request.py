import requests

url = 'https://api.coingecko.com/api/v3/simple/price'
COINS = ['bitcoin', 'ethereum', 'binancecoin', 'tether', 'cardano', 'dogecoin', 'polkadot', 'usd-coin',
         'uniswap']


def get_coin_rate(coin):
    try:
        params = {f'ids': coin, 'vs_currencies': 'usd', 'include_24hr_change': 'true'}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        price = data[coin]['usd']
        change = data[coin]['usd_24h_change']
        return f"{coin.capitalize()}: ${price:.2f} (24h change: {change or ''}%)"
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


def is_correct_coin_name(coin):
    try:
        params = {f'ids': coin.lower(), 'vs_currencies': 'usd', 'include_24hr_change': 'true'}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        if data[coin] is not None:
            return True
        else:
            return False
    except Exception as e:
        return False