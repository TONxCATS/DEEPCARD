from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("7793220413: AAFQkchWGM3B4RL lUrDf
11FYzeonN1rljGo")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(" Welcome DEEP Card Bot 🚀")

async def main():
    await dp.start_polling(bot)

if name == "__main__":
    asyncio.run(main())
