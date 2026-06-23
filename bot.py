import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from database.db import init_db
from handlers import common, menu

load_dotenv()

async def main():
    # Инициализируем базу данных при старте
    init_db()
    
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()
    
    # Регистрируем роутеры
    dp.include_router(common.router)
    dp.include_router(menu.router)
    
    print("Бот успешно запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен.")