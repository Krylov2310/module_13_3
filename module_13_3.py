from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio


"""
Задание выполнялось на:
Phiton 3.9
aiogram 2.25
"""

user_token = input('Введите ваш токен: ')
bot = Bot(token=user_token)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=["help"])
async def greeting(message):
    text = ('2024/01/19 00:00|Домашнее задание по теме "Методы отправки сообщений".'
            '\nЦель: написать простейшего телеграм-бота, используя асинхронные функции.'
            '\nЗадача "Он мне ответил!":'
            '\nСтудент Крылов Эдуард Васильевич.'
            '\nДата работы над заданием: 16.10.2024г.')
    await message.answer(text)


@dp.message_handler(commands=["start"])
async def start_message(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")


@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, или /help чтобы начать общение.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
