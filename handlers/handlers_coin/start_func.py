from aiogram import types, Dispatcher
from keyboard.menu import menu_item




async def start_func(message: types.Message):
    menu = types.InlineKeyboardMarkup(row_width=1)
    menu.add(*menu_item)
    await message.answer(f"Приветствую вас, {message.from_user.first_name}! Рад вам помочь)", reply_markup=menu)


def register_start_func(dp: Dispatcher):
    dp.register_message_handler(start_func, commands=["start"])
