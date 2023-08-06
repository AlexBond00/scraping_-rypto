from aiogram import types, Dispatcher
from aiogram.dispatcher.storage import FSMContext
from scraping.scraping_info import date_added_coin


async def date_added(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    added_data = await date_added_coin(data["coin"])
    await call.message.answer(added_data)


def register_date_added(dp: Dispatcher):
    dp.register_callback_query_handler(date_added, lambda callback: callback.data == "date_added")
