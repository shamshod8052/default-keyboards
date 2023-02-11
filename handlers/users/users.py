from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from handlers.users.start import hamma
from keyboards.default.menuKeyboard import boshla
from loader import dp
from utils.telegraph import photo_link


@dp.message_handler(text='Users')
async def bot_start(message: types.Message):
    users = InlineKeyboardMarkup()
    for i in hamma:
        tugma = InlineKeyboardButton(text=hamma[i][0], url=f"tg://user?id={i}")
        users.add(tugma)
    await message.answer('Users', reply_markup=users)

@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def bot_start(message: types.Message):
    photo = message.photo[-1]
    link = await photo_link(photo)
    await message.answer(link)

