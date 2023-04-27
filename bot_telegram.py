from aiogram.utils import executor
from create_bot import dp
from database import sqlitedb
from states import sql_add_command




async def on_startup(_):
    print("Bot is Online")
    sqlitedb.sql_start()
from handlers import client
from handlers import admin
from handlers import sqlite
client.register_handlers_client(dp)
#other.register_handlers_other(dp)
admin.register_message_handler(dp)
sqlitedb.register_message_handler(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)