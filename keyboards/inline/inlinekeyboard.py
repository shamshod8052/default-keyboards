from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_data import course_callback, book_callback
from loader import dp, bot

categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kurslar", callback_data="courses"),
            InlineKeyboardButton(text="Kitoblar", callback_data="books")
        ],
        [
            InlineKeyboardButton(text="Mohirdev sahifasiga o'tish", url="https://mohirdev.uz/courses/")
        ],
        [
            InlineKeyboardButton(text="Qidirish", switch_inline_query_current_chat="")
        ],
        [
            InlineKeyboardButton(text="Ulashish", switch_inline_query="\nZo'r bot ekan")
        ]
    ]
)

#Kurslar uchun keyboard
coursesMenu = InlineKeyboardMarkup(row_width=1)

python = InlineKeyboardButton(text="Python dasturlash asoslari", callback_data=course_callback.new(item_name="python"))
django = InlineKeyboardButton(text="Django web dasturlash", callback_data=course_callback.new(item_name="django"))
telegram = InlineKeyboardButton(text="Mukamal telegram bot", callback_data=course_callback.new(item_name="telegram"))
algorithm = InlineKeyboardButton(text="Ma'lumotlar tuzilmasi va algoritmlar", callback_data="course:algorithm")
back_button = InlineKeyboardButton(text="Orqaga", callback_data="course:back")
coursesMenu.insert(python)
coursesMenu.insert(django)
coursesMenu.insert(telegram)
coursesMenu.insert(algorithm)
coursesMenu.insert(back_button)

books = {
    "Python. Dasturlash asoslari": "python_book",
    "C++. Dasturlash tili": "cpp_book",
    "Mukammal Dasturlash.Javascript": "js_book"
}

booksMenu = InlineKeyboardMarkup(row_width=2)
for key, value in books.items():
    booksMenu.insert(InlineKeyboardButton(text=key, callback_data=book_callback.new(item_name=value)))
booksMenu.insert(back_button)


#Har bir kurs uchun tugma

telegram_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Xarid qilish", url="https://mohirdev.uz/courses/telegram/")
        ]
    ]
)

algorithm_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ko'rish", url="https://mohirdev.uz/courses/algoritmlar/")
        ]
    ]
)





@dp.inline_handler(lambda inline_query: inline_query.query == 'switch')
async def switch_inline_handler(inline_query: types.InlineQuery):
    results = [
        types.InlineQueryResultArticle(
            id='1',
            title='Switch to a different chat',
            input_message_content=types.InputTextMessageContent(
                message_text='Switching to a different chat...'
            )
        )
    ]
    await bot.answer_inline_query(inline_query.id, results, switch_pm_text='Switch', switch_pm_parameter='1')











