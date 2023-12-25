from loader import dp
from keyboards.inline.alloqa import alloqab
from aiogram import types

@dp.message_handler(text="📞 Aloqa")
async def allqaf(message:
	types.Message):
	await message.answer("<b>✅ Qo'llab Quvvatlash Markazi:\n\nℹ️ Agarda sizda bizni servisimizga oid savol va takliflar mavjud bo'lsa yoki siz almashuvingiz haqida ko'proq ma'lumotga ega bo'lmoqchi bo'lsangiz, bemalol murojat qilishingiz mumkin.\n\n♻️ Almashuvlar operator tomonidan navbati bilan amalga oshiriladi va 2 daqiqadan 60 daqiqagacha davom etadi!</b>",reply_markup=alloqab)
