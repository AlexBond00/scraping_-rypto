from aiogram import Dispatcher
from handlers.handlers_coin.all_info_coin import *


def register_all_info(dp: Dispatcher):
    register_price(dp)
    register_market_cap(dp)
    register_volume(dp)
    register_date_added(dp)
    register_percent_change(dp)
    register_circulating_supply(dp)
    register_back(dp)

