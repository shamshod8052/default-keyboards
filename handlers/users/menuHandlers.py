import logging
from aiogram.types import Message, CallbackQuery
from keyboards.inline import callback_data
from keyboards.inline.callback_data import course_callback, book_callback
from keyboards.inline.inlinekeyboard import categoryMenu, coursesMenu, booksMenu, telegram_keyboard
from loader import dp

@dp.message_handler(text_contains="Mahsulotlar")
async def select_category(message: Message):
    await message.answer(f"Mahsulotni tanlang", reply_markup=categoryMenu)

@dp.callback_query_handler(text="courses")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Kursni tanlang", reply_markup=coursesMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="books")
async def buy_books(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Kitobni tanlang", reply_markup=booksMenu)
    await call.answer(cache_time=60)

#CallbackData yordamida filtrlash
@dp.callback_query_handler(course_callback.filter(item_name="telegram"))
async def buy_books(call: CallbackQuery):
    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")
    await dp.bot.send_message("1019133305", f"Salom {call.from_user.id}")
    await call.message.answer("Siz Mukammal Telegram Bot kursini tanladingiz.", reply_markup=telegram_keyboard)
    await call.answer(cache_time=1)

@dp.callback_query_handler(book_callback.filter(item_name="python_book"))
async def buy_python(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.answer("Buyurtmangiz qabul qilindi", cache_time=60, show_alert=False)

@dp.callback_query_handler(text="course:back")
async def cancel(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=categoryMenu)
    await call.answer()
