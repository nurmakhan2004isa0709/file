from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import  types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from database import sqlitedb
from keyboards import admin_kb

ID = 1024402075

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    discription =  State()
    staj = State()

@dp.message_handler(commands=['Moderator'], is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    if message.from_user.id != ID:
        await bot.send_message((message.from_user.id, ""))
    await bot.send_message(message.from_user.id, "ne kerek",reply_markup=admin_kb.button_case_admin)
    await message.delete()

@dp.message_handler(commands='Barber_qosu', state=None)
async def cm_start(message : types.Message):
    if message.from_user.id == ID:
        await   FSMAdmin.photo.set()
        await message.reply('Zagruzki foto')

@dp.message_handler(state="*", commands='otmena')
@dp.message_handler(Text(equals="otmena", ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply("OK")

@dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply("Malimeti")

@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply("sipattama")

@dp.message_handler(state=FSMAdmin.name)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply("Masterdin stajin engiz")

@dp.message_handler(state=FSMAdmin.name)
async def load_staj(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['staj'] = float(message.text)

        await sqlite_db.sql_add_command(state)
    #sql_add(state)
        await state.finish()





#registratsiya hendler
def register_message_handler(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['zagruzit'], state=None)
    dp.register_message_handler(cancel_handler, Text(equals='otmena',ignore_case=True), state="*")
    dp.register_message_handler(make_changes_command, commands=['Moderator'], is_chat_admin=True)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.discription)
    dp.register_message_handler(load_staj, state=FSMAdmin.staj)
    dp.register_message_handler(cancel_handler, state="*", commands="otmena")
