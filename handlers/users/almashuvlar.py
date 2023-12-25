from loader import dp
from keyboards.inline.almashuvk import almashuvb
from aiogram import types

@dp.message_handler(text="♻️ Almashuvlar")
async def almashuvf(message:
	types.Message):
	await message.answer("<b>Bizning barcha almashuvlar kanali ⤵️</b>",reply_markup=almashuvb)
