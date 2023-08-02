import asyncio
from scraping.api_cmc import getInfo, id_coin
# from scraping.api_cmc import info_fanc


def price_coin(coin):
    info_func = asyncio.run(getInfo(coin))
    name = info_func['data'][f'{id_coin[coin]}']['name']
    price = info_func['data'][f'{id_coin[coin]}']['quote']['USD']['price']
    return f'Цена {name} = {round(price, 2)} USD.'


def date_added_coin(coin):
    date_added = asyncio.run(getInfo(coin))['data'][f'{id_coin[coin]}']['date_added']
    return f'Дата создания монеты = {date_added}'


def circulating_supply_coins(coin):
    circulating_supply = asyncio.run(getInfo(coin))['data'][f'{id_coin[coin]}']['circulating_supply']
    return f'На рынке циркулирует {circulating_supply} монет.'


def percent_change_24h(coin):
    percent_change = asyncio.run(getInfo(coin))['data'][f'{id_coin[coin]}']['quote']['USD']['percent_change_24h']
    return f'Изменение цены за последнии сутки: {percent_change} USD.'


def volume_24h(coin):
    volume = asyncio.run(getInfo(coin))['data'][f'{id_coin[coin]}']['quote']['USD']['volume_24h']
    return f'Объем торгов за последнии сутки: {round(volume, 2)} USD.'


def market_cap_coin(coin):
    name = asyncio.run(getInfo(coin))['data'][f'{id_coin[coin]}']['name']
    market_cap = asyncio.run(getInfo(coin))['data'][f'{id_coin[coin]}']['quote']['USD']['market_cap']
    return f'Капитализация {name}: {round(market_cap, 2)} USD.'











