from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Mahsulotlar"),
            KeyboardButton(text="Qo'lanma")
        ]
    ],
    resize_keyboard=True
)