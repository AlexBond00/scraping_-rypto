import asyncio
from scraping.api_cmc import getInfo, id_coin



async def price_coin(coin):
    info_func = await getInfo(coin)
    name = info_func['data'][f'{id_coin[coin]}']['name']
    price = info_func['data'][f'{id_coin[coin]}']['quote']['USD']['price']
    return f'Цена {name} = {round(price, 2)} USD.'


async def date_added_coin(coin):
    info_func = await getInfo(coin)
    date_added = info_func['data'][f'{id_coin[coin]}']['date_added']
    return f'Дата создания монеты = {date_added}'


async def circulating_supply_coins(coin):
    info_func = await getInfo(coin)
    circulating_supply = info_func['data'][f'{id_coin[coin]}']['circulating_supply']
    return f'На рынке циркулирует {circulating_supply} монет.'


async def percent_change_24h(coin):
    info_func = await getInfo(coin)
    percent_change = info_func['data'][f'{id_coin[coin]}']['quote']['USD']['percent_change_24h']
    return f'Изменение цены за последнии сутки: {percent_change} USD.'


async def volume_24h(coin):
    info_func = await getInfo(coin)
    volume = info_func['data'][f'{id_coin[coin]}']['quote']['USD']['volume_24h']
    return f'Объем торгов за последнии сутки: {round(volume, 2)} USD.'


async def market_cap_coin(coin):
    info_func = await getInfo(coin)
    name = info_func['data'][f'{id_coin[coin]}']['name']
    market_cap = asyncio.run(getInfo(coin))['data'][f'{id_coin[coin]}']['quote']['USD']['market_cap']
    return f'Капитализация {name}: {round(market_cap, 2)} USD.'











