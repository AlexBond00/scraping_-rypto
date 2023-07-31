import logging
from aiogram import executor
from creat_bot import dp
from handlers import coin_list, start_func, coin_information, all_register_info


logging.basicConfig(level=logging.INFO)

start_func.register_start_func(dp)
coin_list.register_coin_list(dp)
coin_information.register_coin_information(dp)
all_register_info.register_all_info(dp)




def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()

