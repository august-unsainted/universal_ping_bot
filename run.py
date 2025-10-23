import asyncio
from aiogram import Bot, Dispatcher
from handlers import all, developers

from config import TOKEN
from utils.get_members import on_startup, on_shutdown

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_routers(all.router, developers.router)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
