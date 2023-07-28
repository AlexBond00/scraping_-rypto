from scraping.api_cmc import getInfo, id_coin


def price_coin(coin):
    name = getInfo(coin=coin)['data'][f'{id_coin[coin]}']['name']
    price = getInfo(coin=coin)['data'][f'{id_coin[coin]}']['quote']['USD']['price']
    return f'Цена {name} = {round(price, 2)} USD.'


def date_added_coin(coin):
    date_added = getInfo(coin=coin)['data'][f'{id_coin[coin]}']['date_added']
    return f'Дата создания монеты = {date_added}'


def circulating_supply_coins(coin):
    circulating_supply = getInfo(coin=coin)['data'][f'{id_coin[coin]}']['circulating_supply']
    return f'На рынке циркулирует {circulating_supply} монет.'


def percent_change_24h(coin):
    percent_change = getInfo(coin=coin)['data'][f'{id_coin[coin]}']['quote']['USD']['percent_change_24h']
    return f'Изменение цены за последнии сутки: {percent_change} USD.'


def volume_24h(coin):
    volume = getInfo(coin=coin)['data'][f'{id_coin[coin]}']['quote']['USD']['volume_24h']
    return f'Объем торгов за последнии сутки: {round(volume, 2)} USD.'


def market_cap_coin(coin):
    name = getInfo(coin=coin)['data'][f'{id_coin[coin]}']['name']
    market_cap = getInfo(coin=coin)['data'][f'{id_coin[coin]}']['quote']['USD']['market_cap']
    return f'Капитализация {name}: {round(market_cap, 2)} USD.'










# print(price('bitcoin'))




#
# date_added = all_info['data'][f'{id_coin[call.data]}']['date_added']
# circulating_supply = all_info['data'][f'{id_coin[call.data]}']['circulating_supply']
# percent_change_24h = all_info['data'][f'{id_coin[call.data]}']['quote']['USD']['percent_change_24h']
# volume_24h = all_info['data'][f'{id_coin[call.data]}']['quote']['USD']['volume_24h']
# market_cap = all_info['data'][f'{id_coin[call.data]}']['quote']['USD']['market_cap']

