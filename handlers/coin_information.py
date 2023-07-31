from aiogram import types, Dispatcher
from keyboard.coin_info import coin_info
from scraping.api_cmc import id_coin
from aiogram.dispatcher.storage import FSMContext



async def coin_information(call: types.CallbackQuery, state: FSMContext):
    info_coins = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    await state.update_data(coin=call.data)

    info_coins.add(*coin_info)
    await call.message.answer(f"Здесь вы можете найти необходимую информацию о монете - {call.data}."
                              f" \n Выберите, что бы вы хотели узнать!)", reply_markup=info_coins)



def register_coin_information(dp: Dispatcher):
    dp.register_callback_query_handler(coin_information, lambda callback: callback.data in id_coin.keys())

