from io import BytesIO
from aiogram import types
from loader import bot
import aiohttp
async def photo_link(photo: types.photo_size.PhotoSize):
    with await photo.download(BytesIO()) as file:
        form = aiohttp.FormData()
        form.add_field(
            name='file',
            value=file
        )
        async with bot.session.post('https://telegra.ph/upload', data=form) as response:
            img_src = await response.json()
    print(img_src)
    link = 'https://telegra.ph' + img_src[0]['src']
    return link
