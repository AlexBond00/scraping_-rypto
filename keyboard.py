from aiogram import types

menu_item = [
        types.InlineKeyboardButton(text="Инфрмация о монетаx", callback_data="coin_list"),
        types.InlineKeyboardButton(text="Новости", callback_data="news"),
        types.InlineKeyboardButton(text="О боте", callback_data="about_bot")
]


coin = [
        types.InlineKeyboardButton(text="bitcoin", callback_data="bitcoin"),
        types.InlineKeyboardButton(text="ethereum", callback_data="ethereum"),
        types.InlineKeyboardButton(text="tether", callback_data="tether"),
        types.InlineKeyboardButton(text="bnb", callback_data="bnb"),
        types.InlineKeyboardButton(text="cardano", callback_data="cardano"),
        types.InlineKeyboardButton(text="polygon", callback_data="polygon"),
        types.InlineKeyboardButton(text="toncoin", callback_data="toncoin"),
        types.InlineKeyboardButton(text="tron", callback_data="tron"),
        types.InlineKeyboardButton(text="dogecoin", callback_data="dogecoin")
    ]

coin_info = [
        types.InlineKeyboardButton(text="Цена", callback_data="price"),
        types.InlineKeyboardButton(text="Дата создания", callback_data="date_added"),
        types.InlineKeyboardButton(text="Кол-во монет", callback_data="circulating_supply"),
        types.InlineKeyboardButton(text="Изменение цены за 24ч", callback_data="percent_change"),
        types.InlineKeyboardButton(text="Объем торгов за 24ч", callback_data="volume"),
        types.InlineKeyboardButton(text="Капитализация", callback_data="market_cap")
]