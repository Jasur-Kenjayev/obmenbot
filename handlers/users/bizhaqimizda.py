from loader import dp
from aiogram import types

@dp.message_handler(text="🗞 Biz haqimizda")
async def bizha(message:
	types.Message):
	await message.answer("<b>@obmennbot - Bu O'zbekiston hududidagi ishonchli elektron Pullar(Valyuta) Almashuv Servisi!\n\n👨🏻‍💻 Dasturchi: @Python_Koders</b>")
