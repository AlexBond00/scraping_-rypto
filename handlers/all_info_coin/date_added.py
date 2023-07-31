from aiogram import types, Dispatcher
from aiogram.dispatcher.storage import FSMContext
from scraping.scraping_info import date_added_coin


async def date_added(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await call.message.answer(date_added_coin(data["coin"]))


def register_date_added(dp: Dispatcher):
    dp.register_callback_query_handler(date_added, lambda callback: callback.data == "date_added")
