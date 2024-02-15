from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

command_router = Router()

@command_router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Assalomu alaykum!\n\nBotga xush kelibsiz")


@command_router.message(Command('help'))
async def help_handler(message: Message):
    await message.answer("How can I help you?")
