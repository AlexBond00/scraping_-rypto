from aiogram import types


coin_info = [
        types.InlineKeyboardButton(text="Цена", callback_data="price"),
        types.InlineKeyboardButton(text="Дата создания", callback_data="date_added"),
        types.InlineKeyboardButton(text="Кол-во монет", callback_data="circulating_supply"),
        types.InlineKeyboardButton(text="Изменение цены за 24ч", callback_data="percent_change"),
        types.InlineKeyboardButton(text="Объем торгов за 24ч", callback_data="volume"),
        types.InlineKeyboardButton(text="Капитализация", callback_data="market_cap"),
        types.InlineKeyboardButton(text="Назад", callback_data="back")
]
