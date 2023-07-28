from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from scraping.scraping_info import price_coin, date_added_coin, circulating_supply_coins, percent_change_24h, volume_24h, market_cap_coin
from keyboard import menu_item, coin, coin_info
import logging
from aiogram import Bot, Dispatcher, types, executor
from scraping.api_cmc import id_coin
from config import TOKEN_API


logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def cmd_random(message: types.Message):
    menu = types.InlineKeyboardMarkup(row_width=1)
    menu.add(menu_item)
    await message.answer(f"Приветствую вас, {message.from_user.first_name}! Рад вам помочь)", reply_markup=menu)


@dp.callback_query_handler(text="coin_list")
async def coin_list(call: types.CallbackQuery):
    coins = types.InlineKeyboardMarkup(resize_keyboard=True)
    coins.add(*coin)
    await call.message.answer("Выберите интересующую вас монету:", reply_markup=coins)


@dp.callback_query_handler(text=id_coin.keys())
async def coin_information(call: types.CallbackQuery):
    info_coins = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    info_coins.add(*coin_info)
    await call.message.answer(f"Здесь вы можете найти необходимую информацию о монете - {call.data} ."
                              f" \n Выберите, что бы вы хотели узнать!)", reply_markup=info_coins)


@dp.callback_query_handler()
async def price(call: types.CallbackQuery):
    name_coin = call.message.text.split()
    if call.data == "price":
        await call.message.answer(price_coin(name_coin[9]))
    elif call.data == "date_added":
        await call.message.answer(date_added_coin(name_coin[9]))
    elif call.data == "circulating_supply":
        await call.message.answer(circulating_supply_coins(name_coin[9]))
    elif call.data == "percent_change":
        await call.message.answer(percent_change_24h(name_coin[9]))
    elif call.data == "volume":
        await call.message.answer(volume_24h(name_coin[9]))
    elif call.data == "market_cap":
        await call.message.answer(market_cap_coin(name_coin[9]))






def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()

