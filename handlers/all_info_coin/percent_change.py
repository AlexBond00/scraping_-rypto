from aiogram import types, Dispatcher
from aiogram.dispatcher.storage import FSMContext
from scraping.scraping_info import percent_change_24h


async def percent_change(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    change_percent = await percent_change_24h(data["coin"])
    await call.message.answer(change_percent)


def register_percent_change(dp: Dispatcher):
    dp.register_callback_query_handler(percent_change, lambda callback: callback.data == "percent_change")
