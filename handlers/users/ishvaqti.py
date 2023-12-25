from loader import dp
from aiogram import types

@dp.message_handler(text="🕘 Ish vaqti")
async def ishvaq(message:
	types.Message):
	await message.answer("<b>⏰Ish vaqti:\n\n♻️Dushanba-Shanbagacha\n♻️07:00 - 22:00\n\n⏰Yakshanba:\n✅Erkin ish vaqti</b>")
