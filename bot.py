import os
import asyncio
from flask import Flask
from aiogram import Bot, Dispatcher, types

app = Flask(__name__)

# Render health-check
@app.route("/")
def home():
    return "Kaspi Analytic Bot is running!"

TOKEN = os.getenv("API_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Бот работает на Render.\nКоманды:\n/update\n/niches\n/trend <ID>")

@dp.message(commands=["update"])
async def update(message: types.Message):
    await message.answer("Обновление данных... (тут потом добавим логику)")

@dp.message(commands=["niches"])
async def niches(message: types.Message):
    await message.answer("ТОП ниш... (добавим позже)")

@dp.message(commands=["trend"])
async def trend(message: types.Message):
    await message.answer("График цены... (тоже добавим позже)")

async def run_bot():
    await dp.start_polling(bot)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(run_bot())
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
