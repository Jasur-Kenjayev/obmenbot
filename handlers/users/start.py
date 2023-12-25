import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu import Menu

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    await message.answer("<b>🤖 @obmennbot - bu O'zbekiston hududidagi ishonchli valyuta almashuv Servisi ✅</b>",reply_markup=Menu)
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg = f"<b>{message.from_user.full_name} 💡Bazaga yangi 👤foydalanuvchi ➕qo'shildi\nBazada {count} ta foydalanuvchi bor✅</b>"
    await bot.send_message(chat_id=ADMINS[0], text=msg)