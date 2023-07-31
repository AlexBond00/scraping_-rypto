from aiogram import types, Dispatcher
from aiogram.dispatcher.storage import FSMContext
from scraping.scraping_info import volume_24h


async def volume(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await call.message.answer(volume_24h(data["coin"]))


def register_volume(dp: Dispatcher):
    dp.register_callback_query_handler(volume, lambda callback: callback.data == "volume")
