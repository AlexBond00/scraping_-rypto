from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from scraping.scraping_info import price_coin, date_added_coin, circulating_supply_coins, percent_change_24h, volume_24h, market_cap_coin
import logging
from aiogram import Bot, Dispatcher, types, executor
from scraping.api_cmc import id_coin
from config import TOKEN_API


logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

coin = [
        types.InlineKeyboardButton(text="bitcoin", callback_data="bitcoin"),
        types.InlineKeyboardButton(text="ethereum", callback_data="ethereum"),
        types.InlineKeyboardButton(text="tether", callback_data="tether"),
        types.InlineKeyboardButton(text="bnb", callback_data="bnb"),
        types.InlineKeyboardButton(text="cardano", callback_data="cardano"),
        types.InlineKeyboardButton(text="polygon", callback_data="polygon"),
        types.InlineKeyboardButton(text="toncoin", callback_data="toncoin"),
        types.InlineKeyboardButton(text="tron", callback_data="tron"),
        types.InlineKeyboardButton(text="dogecoin", callback_data="dogecoin")
    ]

coin_info = [
        types.InlineKeyboardButton(text="Цена", callback_data="price"),
        types.InlineKeyboardButton(text="Дата создания", callback_data="date_added"),
        types.InlineKeyboardButton(text="Кол-во монет", callback_data="circulating_supply"),
        types.InlineKeyboardButton(text="Изменение цены за 24ч", callback_data="percent_change"),
        types.InlineKeyboardButton(text="Объем торгов за 24ч", callback_data="volume"),
        types.InlineKeyboardButton(text="Капитализация", callback_data="market_cap")
]




@dp.message_handler(commands="start")
async def cmd_random(message: types.Message):
    menu = types.InlineKeyboardMarkup(row_width=1)
    menu.add(types.InlineKeyboardButton(text="Инфрмация о монетах", callback_data="coin_list"),
                 types.InlineKeyboardButton(text="Новости", callback_data="news"),
                 types.InlineKeyboardButton(text="О боте", callback_data="about_bot"))
    await message.answer("Приветствую вас! Рад вам помочь)", reply_markup=menu)


@dp.callback_query_handler(text="coin_list")
async def coin_list(call: types.CallbackQuery):
    coins = types.InlineKeyboardMarkup(resize_keyboard=True)
    coins.add(*coin)
    await call.message.answer("Выберите интересующую вас монету:", reply_markup=coins)


@dp.callback_query_handler(text=id_coin.keys())
async def coin_information(call: types.CallbackQuery):
    info_coins = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    info_coins.add(*coin_info)
    await call.message.answer(f"Что вы хотите узнать о {call.data} ?", reply_markup=info_coins)


@dp.callback_query_handler(text="price")
async def price(call: types.CallbackQuery):
    name_coin = call.message.text.split()
    await call.message.answer(price_coin(name_coin[-2]))


@dp.callback_query_handler(text="date_added")
async def date_added(call: types.CallbackQuery):
    name_coin = call.message.text.split()
    await call.message.answer(date_added_coin(name_coin[-2]))


@dp.callback_query_handler(text="circulating_supply")
async def circulating_supply(call: types.CallbackQuery):
    name_coin = call.message.text.split()
    await call.message.answer(circulating_supply_coins(name_coin[-2]))


@dp.callback_query_handler(text="percent_change")
async def percent_change(call: types.CallbackQuery):
    name_coin = call.message.text.split()
    await call.message.answer(percent_change_24h(name_coin[-2]))


@dp.callback_query_handler(text="volume")
async def volume(call: types.CallbackQuery):
    name_coin = call.message.text.split()
    await call.message.answer(volume_24h(name_coin[-2]))


@dp.callback_query_handler(text="market_cap")
async def market_cap(call: types.CallbackQuery):
    name_coin = call.message.text.split()
    await call.message.answer(market_cap_coin(name_coin[-2]))



# @dp.message_handler()
# async def start(message: Message):
#     keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(*id_coin.keys())
#     if message.text == "Список монет":
#         await message.answer("Приветствую вас! Выберите монету, о которой хотели бы получить информацию", reply_markup=keyboard)

#
# @dp.message_handler(commands="Список монет")
# async def coin_info(message: Message):
#     print(message.text)
#     if message.text in id_coin.keys():
#         # await message.answer("Пожалуйста, подождите...")
#
#         all_info = getInfo(coin=message.text)
#
#         price = all_info['data'][f'{id_coin[message.text]}']['quote']['USD']['price']
#         name = all_info['data'][f'{id_coin[message.text]}']['name']
#         date_added = all_info['data'][f'{id_coin[message.text]}']['date_added']
#         circulating_supply = all_info['data'][f'{id_coin[message.text]}']['circulating_supply']
#         percent_change_24h = all_info['data'][f'{id_coin[message.text]}']['quote']['USD']['percent_change_24h']
#         volume_24h = all_info['data'][f'{id_coin[message.text]}']['quote']['USD']['volume_24h']
#         market_cap = all_info['data'][f'{id_coin[message.text]}']['quote']['USD']['market_cap']
#
#         await message.answer(f'Цена {name} = {round(price, 2)} USD.\n'
#                              f'На рынке циркулирует {circulating_supply} монет.\n'
#                              f'Капитализация: {round(market_cap, 2)} USD.\n'
#                              f'Изменение цены за последнии сутки: {percent_change_24h} USD.\n'
#                              f'Объем торгов за последнии сутки: {round(volume_24h, 2)} USD.\n'
#                              f'Дата создания монеты = {date_added}'
#                              )
#
#     await message.delete()



def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()

