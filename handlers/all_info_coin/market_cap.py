from aiogram import types, Dispatcher
from aiogram.dispatcher.storage import FSMContext
from scraping.scraping_info import market_cap_coin


async def market_cap(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await call.message.answer(market_cap_coin(data["coin"]))


def register_market_cap(dp: Dispatcher):
    dp.register_callback_query_handler(market_cap, lambda callback: callback.data == "market_cap")
