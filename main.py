from dotenv import dotenv_values
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

dp = Dispatcher()
env = dotenv_values('.env')


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f'Привет, *{message.from_user.full_name}*!')


@dp.message()
async def normal_message(message: Message):
    await message.answer(f'Привет, *{message.from_user.full_name}*!')




async def main() -> None:
    bot = Bot(token=env['TOKEN'],
              default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
