import pytest

from project import crypto_api_request


def test_cg_coins_list(cg):
    coins_list = cg.get_coins_list()
    assert isinstance(coins_list, list)
    assert len(coins_list) > 0


@pytest.mark.parametrize('coin_name', ['bitcoin', 'ethereum', 'binancecoin', 'tether', 'cardano', 'dogecoin',
                                       'polkadot', 'usd-coin', 'uniswap'])
def test_get_coin_by_id(coin_name):
    coin = crypto_api_request.get_coin_rate(coin_name)
    assert isinstance(coin, str)
    assert '24h change:' in coin
    assert 'low_24h:' in coin
    assert 'high_24h:' in coin


@pytest.mark.parametrize('coin_name', ['bitcoin', 'ethereum', 'binancecoin', 'tether', 'cardano', 'dogecoin',
                                       'polkadot', 'usd-coin', 'uniswap'])
def test_is_correct_coin_name(coin_name):
    is_correct = crypto_api_request.is_correct_coin_name(coin_name)
    assert is_correct is True
