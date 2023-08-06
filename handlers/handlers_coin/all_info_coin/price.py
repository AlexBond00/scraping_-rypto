from aiogram import types, Dispatcher
from aiogram.dispatcher.storage import FSMContext
# from scraping.scraping_info import price_coin
from scraping.scraping_info import price_coin


async def price(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    coin_price = await price_coin(data["coin"])
    await call.message.answer(coin_price)


def register_price(dp: Dispatcher):
    dp.register_callback_query_handler(price, lambda callback: callback.data == "price")
