from aiogram import types, Dispatcher
from aiogram.dispatcher.storage import FSMContext
from scraping.scraping_info import price_coin


async def price(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    print(data)
    await call.message.answer(price_coin(data["coin"]))


def register_price(dp: Dispatcher):
    dp.register_callback_query_handler(price, lambda callback: callback.data == "price")
