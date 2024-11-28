from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.filters.command import Command
from aiogram import F

TOKEN = None
with open("token2.txt") as f:
    TOKEN = f.read().strip()

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def startCommand(message: types.Message):
    await message.answer("ТРАНСФОРМИРУЮСЬ")

@dp.message(F.voice)
async def voiceFilter(message: types.message):
    await message.answer("ААААА ТЫ РАЗГОВАРИВАЕШЬ")
    
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())