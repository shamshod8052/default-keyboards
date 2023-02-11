from aiogram import types
from aiogram.utils.markdown import hbold, hitalic

from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    # await message.answer(hbold(message.text), parse_mode=types.ParseMode.MARKDOWN_V2)
    await message.answer(hbold(message.text))
