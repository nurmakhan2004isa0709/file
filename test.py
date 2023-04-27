from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.dispatcher import  Dispatcher
import os

from aiogram.types import InlaineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token="6003611308:AAHM5sOuz1sTdZ9w7JV1BZfC2wDNtDONOGk")
dp = Dispatcher(bot, storage=storage)
@dp.message_handler(commands=['start','help'])
async def command_start(message: types.Message):
    await  message.reply('Zdarov')

@dp.message_handler(commands=['commanda'])
async def echo(message: types.Message):
    await message.answer(message,text)

@dp.message_handler()
async def empty(nessage: types.Message):
    await message.answer(message)

urlkb = InlaineKeyboardMarkup(row_with=2)
urlButton = InlineKeyboardButton(text="insta mastera",url=)
urlButton2 = InlineKeyboardButton(text="insta mastera 2",url=)
urlkb.add(urlButton,urlButton2).row(*x)

@dp.message_handler(commands="insta")
async def url_comamand(message: taypes.Messege):
    await message.answer("instagram",reply_markup=urlkb)

executor.start_polling(dp,skip_updates=True)


