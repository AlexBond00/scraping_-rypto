import logging
from aiogram import executor
from creat_bot import dp
from handlers.handlers_coin import all_register_info, coin_information, ico_handler, detail_ico_info
from handlers import start_func, coin_list

logging.basicConfig(level=logging.INFO)

start_func.register_start_func(dp)
coin_list.register_coin_list(dp)
coin_information.register_coin_information(dp)
all_register_info.register_all_info(dp)
ico_handler.register_ico_list(dp)
detail_ico_info.register_ico_all_info(dp)




def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()

