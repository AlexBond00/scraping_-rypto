from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from scraping.scrapy_icodrops import result


async def ico_all_info(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(coin=call.data)
    await call.message.answer(f"Предоставляем вам всю доступную инфорацию о проекте - {call.data}"
                              f"\nСсылка на проект: {result[call.data]['link']}"
                              f"\nКатегория проекта - {result[call.data]['category_coin']}"
                              f"\nИнтерес к проекту - {result[call.data]['interest']}"
                              f"\nСумма собраных средств на проекте - {result[call.data]['received']}"
                              f"\nЦель по сбору средств проекта - {result[call.data]['goal']}"
                              f"\nОсталось дней до конца сборов средств {result[call.data]['date_active']}"
                              )



def register_ico_all_info(dp: Dispatcher):
    dp.register_callback_query_handler(ico_all_info, lambda callback: callback.data in result.keys())

