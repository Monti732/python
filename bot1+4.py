from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.filters.command import Command
from aiogram import F

TOKEN = None
with open("token1.txt") as f:
    TOKEN = f.read().strip()

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.text.lower() == "образовательные платформы и курсы")
async def courses(message: types.Message):
    await message.answer("Coursera — это онлайн-платформа, где ведущие университеты и компании предлагают курсы, специализации и дипломные программы с возможностью получения сертификатов. https://www.coursera.org/")
    await message.answer("Udemy — это образовательная платформа с курсами от независимых преподавателей, охватывающими широкий спектр тем, от программирования до личностного роста. https://www.udemy.com/")

@dp.message(F.text.lower() == "платформы для хостинга и совместной разработки")
async def hostings(message: types.Message):
    await message.answer("GitHub — это платформа для хостинга и совместной разработки программного обеспечения, использующая систему контроля версий Git, с возможностью сотрудничества через репозитории и пулл-реквесты. https://github.com/")
    await message.answer("GitLab — это веб-сервис для хостинга репозиториев, а также для интегрированного управления DevOps процессами, включая CI/CD, тестирование и деплой. https://gitlab.com/")

@dp.message(F.text.lower() == "форумы и сообщества")
async def forums(message: types.Message):
    await message.answer("Stack Overflow — это популярная платформа для программистов, где они могут задавать вопросы, получать ответы, делиться знаниями и находить решения для проблем, связанных с программированием. https://ru.stackoverflow.com/")
    await message.answer("Habr — это русскоязычная платформа для IT-специалистов, где пользователи делятся статьями, новостями, опытом и обсуждают технологии, программирование, науку и бизнес. https://habr.com/")

@dp.message(F.text.lower() == "ресурсы для практики и тестирования навыков")
async def tests(message: types.Message):
    await message.answer("LeetCode — это онлайн-платформа для практики алгоритмов и задач по программированию, популярная среди разработчиков, готовящихся к собеседованиям. https://leetcode.com/")
    await message.answer("HackerRank — это сайт для решения задач по программированию, алгоритмам и интервью, а также для участия в конкурсах и обучении навыкам кодирования. https://www.hackerrank.com/")

@dp.message(F.text.lower() == "убрать клаву")
async def tests(message: types.Message):
    await message.answer("ок",reply_markup=types.ReplyKeyboardRemove())

@dp.message(Command("start"))
async def commandStart(message: types.Message):
    kb = [
        [types.KeyboardButton(text="образовательные платформы и курсы")],
        [types.KeyboardButton(text="платформы для хостинга и совместной разработки")],
        [types.KeyboardButton(text="форумы и сообщества")],
        [types.KeyboardButton(text="ресурсы для практики и тестирования навыков")],
        [types.KeyboardButton(text="убрать клаву")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb) 
    await message.answer("выберите вариант", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
