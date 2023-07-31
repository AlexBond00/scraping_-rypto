from aiogram import types, Dispatcher
from keyboard.menu import menu_item


async def back(call: types.CallbackQuery):
    menu = types.InlineKeyboardMarkup(row_width=1)
    menu.add(*menu_item)
    await call.message.answer("Чем еще могу вам помочь?", reply_markup=menu)


def register_back(dp: Dispatcher):
    dp.register_callback_query_handler(back, lambda callback: callback.data == "back")
