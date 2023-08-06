from aiogram import types, Dispatcher
from keyboard.coin import coin




async def coin_list(call: types.CallbackQuery):
    coins = types.InlineKeyboardMarkup(resize_keyboard=True)
    coins.add(*coin)
    await call.message.answer("Выберите интересующую вас монету:", reply_markup=coins)


def register_coin_list(dp: Dispatcher):
    dp.register_callback_query_handler(coin_list, lambda callback: callback.data == "coin_list")
