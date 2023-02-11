from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


boshla = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Users')
        ]
    ],
    resize_keyboard=True
)

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Mahsulotlar'),
            KeyboardButton(text='Telegram bot')
        ]
    ],
    resize_keyboard=True
)


menuPython = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Darslar'),
            KeyboardButton(text='Kitoblar'),
            KeyboardButton(text='Masalalar')
        ],
        [
            KeyboardButton(text='Bosh menu')
        ]
    ],
    resize_keyboard=True
)


menuBot = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kerakli dasturlar"),
            KeyboardButton(text="Serverga yuklash")
        ],
        [
            KeyboardButton(text="Bosh menu")
        ]
    ],
    resize_keyboard=True
)












