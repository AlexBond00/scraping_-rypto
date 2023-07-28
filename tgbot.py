import json
import logging
from aiogram import Bot, Dispatcher, types, executor
from api_cmc import id_coin, getInfo
from config import TOKEN_API


logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    print(message)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*id_coin.keys())
    await message.answer("Приветствую вас! Выберите монету, о которой хотели бы получить информацию", reply_markup=keyboard)


@dp.message_handler()
async def coin_info(message: types.Message):
    await message.answer("Пожалуйста, подождите...")

    all_info = getInfo(coin=message.text)

    price = all_info['data'][f'{id_coin[message.text]}']['quote']['USD']['price']
    name = all_info['data'][f'{id_coin[message.text]}']['name']
    date_added = all_info['data'][f'{id_coin[message.text]}']['date_added']
    circulating_supply = all_info['data'][f'{id_coin[message.text]}']['circulating_supply']
    percent_change_24h = all_info['data'][f'{id_coin[message.text]}']['quote']['USD']['percent_change_24h']
    volume_24h = all_info['data'][f'{id_coin[message.text]}']['quote']['USD']['volume_24h']
    market_cap = all_info['data'][f'{id_coin[message.text]}']['quote']['USD']['market_cap']

    await message.answer(f'Цена {name} = {round(price, 2)} USD.\n'
                         f'На рынке циркулирует {circulating_supply} монет.\n'
                         f'Капитализация: {round(market_cap, 2)} USD.\n'
                         f'Изменение цены за последнии сутки: {percent_change_24h} USD.\n'
                         f'Объем торгов за последнии сутки: {round(volume_24h, 2)} USD.\n'
                         f'Дата создания монеты = {date_added}'
                         )

    await message.delete()



def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()

