from aiogram import types

menu_item = [
        types.InlineKeyboardButton(text="Инфрмация о монетах", callback_data="coin_list"),
        types.InlineKeyboardButton(text="Новости", callback_data="news"),
        types.InlineKeyboardButton(text="О боте", callback_data="about_bot")
]