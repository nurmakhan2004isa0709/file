from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os 
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()


bot = Bot(token="6003611308:AAHM5sOuz1sTdZ9w7JV1BZfC2wDNtDONOGk")
dp = Dispatcher(bot, storage=storage)