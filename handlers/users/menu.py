from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu, menuPython, menuBot
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    await message.answer("Kurslarni tanlang", reply_markup=menu)

@dp.message_handler(text="Python")
async def python_menu(message: Message):
    await message.answer("Kurslarni tanlang", reply_markup=menuPython)

@dp.message_handler(text="Telegram bot")
async def bot_menu(message: Message):
    await message.answer("Video darslarni ko'ring!", reply_markup=menuBot)

@dp.message_handler(text='Bosh menu')
async def bot_menu(message: Message):
    await message.answer("Bosh menu", reply_markup=menu)

@dp.message_handler(text="Kerakli dasturlar")
async def bot_menu(message: Message):
    await message.answer("Video darsni ko'ring!")
    await message.answer("https://www.youtube.com/watch?v=5qUTBMJLGfM")

@dp.message_handler(text="Serverga yuklash")
async def bot_menu(message: Message):
    await message.answer("Video darsni ko'ring!")
    await message.answer("https://www.youtube.com/watch?v=b6w9lS-OkPo")
