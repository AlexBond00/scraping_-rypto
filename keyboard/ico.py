from scraping.scrapy_icodrops import result
from aiogram import types


def ico_keyboard(result):
    keyboard = []
    keyboard_ico = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=3)
    for key in result.keys():
        keyboard.append(types.InlineKeyboardButton(text=key, callback_data=key))
    keyboard_ico.add(*keyboard)
    return keyboard_ico


keyboard_ico = ico_keyboard(result)
# print(keyboard_ico)