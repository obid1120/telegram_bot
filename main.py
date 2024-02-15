import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import BotCommand

from config import BOT_TOKEN
from handlers import command_handlers # handlers ichidahi fileni tanimayabdi


async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
    await bot.set_my_commands(
        commands=[
            BotCommand(command='start', description='Start/restart bot'),
            BotCommand(command='help', description='Manual for using bot')
        ]
    )
    dp = Dispatcher()
    dp.include_router(command_handlers.command_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
