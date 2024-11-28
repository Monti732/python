from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.filters.command import Command
from aiogram import F

TOKEN = None
with open("token3.txt") as f:
    TOKEN = f.read().strip()

bot = Bot(token=TOKEN)
dp = Dispatcher()

userData = {}

@dp.message(Command("start"))
async def commandStart(message: types.Message):
    kb = [
        [types.KeyboardButton(text="женский")],
        [types.KeyboardButton(text="мужской")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb) 
    await message.answer("Какой ваш пол?", reply_markup=keyboard)

@dp.message(lambda message: message.text.lower() in ["мужской", "женский"])
async def gender(message: types.Message):
    userData["gender"] = message.text
    await message.answer(f"Ваш пол {userData['gender']}, как вас зовут?", reply_markup=types.ReplyKeyboardRemove())

@dp.message(lambda message: message.text and not message.text.isdigit()) 
async def name(message: types.Message):
    userData["name"] = message.text
    await message.answer(f"Твой пол {userData['gender']}, вас зовут {userData['name']}, сколько вам лет?")

@dp.message(lambda message: message.text.isdigit())
async def age(message: types.Message):
    userData["age"] = message.text
    await message.answer(f"Ваш пол {userData['gender']}, вас зовут {userData['name']}, вам {userData['age']} лет")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())