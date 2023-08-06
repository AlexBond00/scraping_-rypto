from aiogram import types, Dispatcher
from keyboard.ico import keyboard_ico


async def ico_list(call: types.CallbackQuery):
    print(call.data)
    await call.message.answer("Здесь вы можете узнать об ативных проектах на стадии ICO. Выберите интересующий вас проект:", reply_markup=keyboard_ico)



def register_ico_list(dp: Dispatcher):
    dp.register_callback_query_handler(ico_list, lambda callback: callback.data == "ico_list")
