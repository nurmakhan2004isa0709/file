from aiogram import types, Dispatcher
from create_bot import  dp, bot
from keyboards import kb_client, kb_menu_client, kb_qyzmetter_menu
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from database import sqlitedb

#@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Qosh keldiniz", reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply("suraq tuyndas habarlasynyz /@Mamoa bot")

#@dp.message_handler(commands=['uaqyty'])
async def barber_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'duysenbi 12-00 jane sarsenbi 13-30 dan 23-.45 ke dein')

#@dp.message_handler(commands=['mekenjai'])
async def barber_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'zhandosov 55', reply_markup=kb_client)

@dp.message_handler(commands=['Menu'])
async def barber_menu_command(message : types.Message):
   await sqlitedb.add.sql_read(messege)
@dp.message_handler(commands='Menu')
async def barber_menu(message: types.Message):
    await message.answer("Menu tizimi", reply_markup=kb_menu_client)

@dp.message_handler(Text(equals="Artqa"))
async def barber_menu(message: types.Message):
    await message.answer("Basty bet", reply_markup=kb_client)

@dp.message_handler(Text(equals="Qyzmetter"))
async def barber_menu(message:types.Message):
    await message.answer("Qyzmetter tizimi", reply_markup=kb_qyzmetter_menu)

@dp.message_handler(Text(equals="aksiyalar"))
async def barber_menu(message: types.Message):
    await message.answer("Bizdegi aksiyalar ote tiymdy\nOlar:\n1)1+1=3\n2)Eger siz tolyq qyzmetten paidalansanyz 20% zhenildik\n3)Student bolsanyz 15% zhenildik", reply_markup=kb_menu_client)

@dp.message_handler(Text(equals="shash_kyskarty"))
async def barber_menu(message:types.Message):
    await message.answer("Bizde shash kyskarty bagalary\n12 jaska deyingi balalarga 1000tg:\n12-16 jaska deingi balalarga 1200tg:\n16 jastan askandarga 1500tg", reply_markup=kb_qyzmetter_menu)

@dp.message_handler(Text(equals="shash_sandey"))
async def barber_menu(message:types.Message):
    await message.answer("Bizde shash sandey baglary\nOkyhylarga 500tg:\nStudentterge 800tg:\nYlkenderge 1000tg", reply_markup=kb_qyzmetter_menu)

@dp.message_handler(Text(equals="sakal_kyskarty"))
async def barber_menu(message:types.Message):
    await message.answer("Bizde sakal kyskarty bagalary\nTolykty okantovkasymen 2000tg:\nPrisheska jasaty 3000tg", reply_markup=kb_qyzmetter_menu)

@dp.message_handler(Text(equals="Betke_maska"))
async def barber_menu(message:types.Message):
    await message.answer("Bizde maskalar bagasy\nKara maska 1000tg:\nSkrab 1000tg:\nGlinnaya maska 1500tg\nMassazh betke 2000tg", reply_markup=kb_qyzmetter_menu)

@dp.message_handler(Text(equals="Shygaring"))
async def barber_menu(message:types.Message):
    await message.answer("Bizde shygaring bagalary\nShygaring betke 1500tg:\nShygaring dlya ysu 500tg\nShygaring dlya tela 5000tg\nShygaring dlya ryki 1500tg obe", reply_markup=kb_qyzmetter_menu)

@dp.message_handler(Text(equals="nazad"))
async def barber_menu(message:types.Message):
    await message.answer("Arqa oralu", reply_markup=kb_menu_client)




def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start','help'])
    dp.register_message_handler(barber_open_command, commands=['uaqyty'])
    dp.register_message_handler(barber_place_command, commands=['mekenjai'])
    dp.register_message_handler(barber_menu_command, commands=['master'])
