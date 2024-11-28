from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio
import aiohttp

TOKEN = None
with open("token5.txt") as f:
    TOKEN = f.read().strip()

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def getUserData():
    async with aiohttp.ClientSession() as session:
        async with session.get(url="https://reqres.in/api/users/2") as response:
            data = await response.json()
            return data

@dp.message(Command("start"))
async def startCommand(message: types.Message):
    await message.answer("Используйте /getUser")

@dp.message(Command("getUser"))
async def getUserCommand(message: types.Message):
    userData = await getUserData()
    user = userData.get("data")
    firstName = user.get("first_name")
    lastName = user.get("last_name")
    userId = user.get("id")
    email = user.get("email")
    avatar = user.get("avatar")
    await message.answer(f"Имя: {firstName}\n Фамилия: {lastName}\n Email: {email}\n Id: {userId}")
    await message.answer_photo(photo=avatar)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())