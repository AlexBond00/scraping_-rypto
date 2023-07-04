import requests
from requests import Request, Session
import json


def getInfo(coin, id_coin):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    api = 'eeea1287-dbda-47da-86ec-ca580fe74b3b'
    parameters = {'slug': f'{coin}',
                  'convert': 'USD'}
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)
    price = json.loads(response.text)['data'][f'{id_coin[coin]}']['quote']['USD']['price']
    date_added = json.loads(response.text)['data'][f'{id_coin[coin]}']['date_added']
    circulating_supply = json.loads(response.text)['data'][f'{id_coin[coin]}']['circulating_supply']
    name = json.loads(response.text)['data'][f'{id_coin[coin]}']['name']
    symbol_network = json.loads(response.text)['data'][f'{id_coin[coin]}']['platform']['name']
    percent_change_24h = json.loads(response.text)['data'][f'{id_coin[coin]}']['quote']['USD']['percent_change_24h']
    volume_24h = json.loads(response.text)['data'][f'{id_coin[coin]}']['quote']['USD']['volume_24h']
    market_cap = json.loads(response.text)['data'][f'{id_coin[coin]}']['quote']['USD']['market_cap']
    # print('Цена: ', price)
    # print('Дата добавления монеты: ', date_added)
    # print('Кол-во монет: ', circulating_supply)
    # print('Название монеты: ', name)
    # print('Сеть: ', symbol_network)
    # print('Рыночная капитализация', market_cap)
    # print('Изменение цены за 24 часа: ', percent_change_24h)
    # print('Объем торгов за последнии 24 часа: ', volume_24h)
    #


id_coin = {
    'bitcoin': 1,
    'ethereum': 1027,
    'tether': 825,
    'bnb': 1839,
    'usd-coin': 3408,
    'xrp': 52,
    'cardano': 2010,
    'dogecoin': 74,
    'litecoin': 2,
    'solana': 5426,
    'tron': 1958,
    'polygon': 3890,
    'polkadot-new': 6636,
    'bitcoin-cash': 1831,
    'toncoin': 11419,
    'wrapped-bitcoin': 3717,
    'multi-collateral-dai': 4943,
    'avalanche': 5805,
    'shiba-inu': 5994,
    'binance-usd': 4687
}

getInfo('shiba-inu', id_coin)
