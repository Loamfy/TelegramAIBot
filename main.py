from dotenv import dotenv_values
import asyncio
import logging
import random

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

dp = Dispatcher()
env = dotenv_values('.env')


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f'Привет! Чтобы я начал говорить, напишите /ai')


@dp.message(Command('ai'))
async def command_start_handler(message: Message) -> None:
    await message.answer(f'Вы начали генерацию сообщений. Чтобы меня остановить, напишите /stop')


@dp.message()
async def on_message(message: Message):
    if random.randint(0, 100) in range(50):
        await message.answer('Подождите.')
        return


async def main() -> None:
    bot = Bot(
        token=env['TOKEN'],
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
    )
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
