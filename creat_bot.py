from aiogram import Bot, Dispatcher
from config import TOKEN_API
from aiogram.contrib.fsm_storage.memory import MemoryStorage



bot = Bot(TOKEN_API)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)



