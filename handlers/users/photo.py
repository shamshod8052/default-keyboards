from aiogram import types
from aiogram.types import InputFile
from loader import dp, bot


@dp.message_handler(text='rasm')
async def sent_photo(message: types.Message):
    photo_link = 'https://telegra.ph/file/f82a1f385ec5eca995206.jpg'
    photo_id = 'AgACAgIAAxkDAAJo0mOZtORBMKea2S5lh6U-6tw9zCQ1AALUwzEbgkzRSLyvrXrKplAdAQADAgADbQADLAQ'
    photo_file = InputFile(path_or_bytesio='photos/python.jpg')
    video_id = 'BAACAgIAAxkDAAJpCWOZuUGUg8VRxk_6cGLuprF1LTU0AALfIgACgkzRSCEz9BjDT1JxLAQ'

    await message.answer_photo(photo_link, caption='bu rasm')
    await message.answer_video(video=video_id, caption='bu video')
    # a = await message.answer_video(open("videos/funny.mp4", 'rb'), caption='bu video')
    # print(a)
    # a = await message.reply_photo(photo_file,caption="sdcdjisfhui")
    # print(a)
    # await bot.send_photo(chat_id=message.from_user.id, photo=photo_id, caption='bu rasm')


@dp.message_handler(text="rasmlar")
async def sent_photo(message: types.Message):
    album = types.MediaGroup()
    photo_link = 'https://telegra.ph/file/f82a1f385ec5eca995206.jpg'
    photo_id = 'AgACAgIAAxkDAAJo0mOZtORBMKea2S5lh6U-6tw9zCQ1AALUwzEbgkzRSLyvrXrKplAdAQADAgADbQADLAQ'
    photo_file = InputFile(path_or_bytesio='photos/python.jpg')
    p = open('photos/python.jpg', 'rb')
    mp3_id ='CQACAgIAAxkBAAOsYyyIObDwT5JoMLPHNCtGB0MEh2IAAqsFAALIsOhItuJKTmi9-W8pBA'
    video_id = 'BAACAgIAAxkDAAJpCWOZuUGUg8VRxk_6cGLuprF1LTU0AALfIgACgkzRSCEz9BjDT1JxLAQ'
    await message.answer_video(video=video_id, caption='bu video')
    album.attach_photo(photo=photo_id)
    album.attach_photo(photo=photo_link)
    album.attach_photo(photo=photo_file)
    # album.attach_many(math=mp3_id)
    album.attach_video(video=video_id, caption="shular ")
    print(album)
    await message.reply_media_group(album)
