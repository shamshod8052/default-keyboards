from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(commands="info_html")
async def bot_help(message: types.Message):
    text = ("<b>Salom</b> <s>Olam</s>")
    await message.answer(text)
