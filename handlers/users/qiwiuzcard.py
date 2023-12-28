import logging
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from loader import dp, bot
from keyboards.inline.Menuin import categoryMenu, qiwiuzcardo
from keyboards.default.menu import Menu
from aiogram.dispatcher import FSMContext
from aiogram import types
from keyboards.inline.manage_post import confirmation_keyboard, post_callback
from states.qiwiuchun import Qiwiu
from data.config import ADMINS
import datetime
import pytz
from aiogram.dispatcher.filters import Command

@dp.message_handler(Command("canceli"),state=Qiwiu)
async def cancel1(message:
	types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>Almashuv bekor qilindi.</b>",reply_markup=Menu)
	
@dp.callback_query_handler(text="rubuzs")
async def rubuzsi1(call: CallbackQuery):
    try:
    	id = call.message.chat.id
    	iduzi = open(f"files/uzcard{id}.txt", "r")
    	qiwiid = open(f"files/qiwi{id}.txt", "r")
    	uzcardzid = open("zahira/uzcardz.txt", "r")
    	uzsz = int(uzcardzid.read())
    	if 5999 < uzsz:
    		await call.message.answer(f"<b>🔄Almashuv:\n\n⬆️Berish: QIWI RUB\n⬇️Olish: UZCARD SUM*\n💳UZCARD: {iduzi.read()}\n💸QIWI: {qiwiid.read()}</b>",reply_markup=qiwiuzcardo)
    		await call.message.delete()
    		await call.answer(cache_time=60)
    	else:
    		await call.answer("ℹ️ Siz tanlagan yo'nalishda almashinuv qilish imkoni hozircha yo'q",show_alert=True)
    	iduzi.close()
    	qiwiid.close()
    	uzcardzid.close()
    except:
    	await call.answer("❗️Siz tanlagan yo'nalishda almashuvni amalga oshirish uchun oldin o'z hamyon raqamlaringizni  '💳 Hamyonlar' bo'limiga kiriting!", show_alert=True)

@dp.callback_query_handler(text_contains="rublqwi")
async def rublq2(call: CallbackQuery):
    uzcardz = open("zahira/uzcardz.txt", "r")
    qiwifo = open("kurs/qiwio.txt", "r")
    uzcardzx = int(uzcardz.read())
    qiwifok = int(qiwifo.read())
    maksimalo = uzcardzx / qiwifok
    natmak = "%.2f" % maksimalo
    await call.message.answer(f"<b>⬆️ Berish miqdorini QIWI RUB da kiriting!\n\nMinimal  50  RUB\nMaksimal {natmak} RUB\n\nBekor qilish uchun: /canceli</b>")
    uzcardz.close()
    qiwifo.close()
    await call.message.delete()
    await call.answer(cache_time=60)
    await Qiwiu.qiwiuch.set()

@dp.message_handler(state=Qiwiu.qiwiuch)
async def hisob2(message: Message,state: FSMContext):
	try:
		qiwiuch = message.text
		await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
		puli2 = int(qiwiuch)
		uzcardzer = open("zahira/uzcardz.txt", "r")
		qiwifoer = open("kurs/qiwio.txt", "r")
		uzcardzxer = int(uzcardzer.read())
		qiwifoker = int(qiwifoer.read())
		maksimaloer = uzcardzxer / qiwifoker
		natijamier = int(maksimaloer)
		songinatijaer = natijamier + 1
		uzcardzer.close()
		qiwifoer.close()
		if 49 < puli2 < songinatijaer:
			id = message.from_user.id
			followrt = open(f"files/uzcard{id}.txt", "r")
			uzcardirt = int(followrt.read())
			qiwirt = open(f"files/qiwi{id}.txt", "r")
			qiwisirt = int(qiwirt.read())
			qiwifort = open("kurs/qiwio.txt", "r")
			qiwifsort = int(qiwifort.read())
			natijarrrt = puli2 * qiwifsort
			natijar2rt = "%.2f" % natijarrrt
			await message.answer("+998935942855")
			msd2 = f"<b>👆Ko'chirib olish uchun. Almashuvingiz muvaffaqiyatli bajarilishi uchun quyidagi harakatlarni amalga oshiring:\n1) Pastda ko'rsatilgan to'lov miqdorni\n\n+998935942452\n\n👆QIWI raqamiga o'tkazing;\n2) «To'lov qildim ✅» tugmasini bosing;\n3) Operator tomonidan almashuv tasdiqlanishini kuting.\n\n📥To'lov miqdori: {qiwiuch} QIWI RUB\n\n📤Olish miqdori: {natijar2rt} UZCARD SUM*\n🇺🇿UZCARD: {uzcardirt}\n🇷🇺QIWI: {qiwisirt}\n\n►Ushbu almashuv operator tomonidan navbati bilan amalga oshiriladi va 2 daqiqadan 60 daqiqagacha davom etadi.</b>"
			await Qiwiu.next()
			await message.answer(msd2,reply_markup=confirmation_keyboard)
			qiwirt.close()
			followrt.close()
			qiwifort.close()
			await state.update_data(
				{"qiwiuch": msd2}
			)
		else:
			uzcardz2 = open("zahira/uzcardz.txt", "r")
			qiwifo2 = open("kurs/qiwio.txt", "r")
			uzcardzx2 = int(uzcardz2.read())
			qiwifok2 = int(qiwifo2.read())
			maksimalo2 = uzcardzx2 / qiwifok2
			natmak2 = "%.2f" % maksimalo2
			await message.answer(f"<b>⬆️ Berish miqdorini QIWI RUB da kiriting!\n\nMinimal  50  RUB\nMaksimal {natmak2} RUB\n\nBekor qilish uchun: /canceli</b>")
			uzcardz2.close()
			qiwifo2.close()
	except:
		await message.answer("<b>❕Butun Son kiriting.</b>")
		
@dp.callback_query_handler(post_callback.filter(action="post"),state=Qiwiu.qiwiuc)
async def confirm_post2(call: CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
        	data = await state.get_data()
        	msd2 = data.get("qiwiuch")
        	msg = f"<b>{msd2}</b>"
        	mention = data.get("mention")
        await state.finish()
        await call.message.edit_reply_markup()
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        pst_now = utc_now.astimezone(pytz.timezone("Asia/Tashkent"))
        dt_string = pst_now.strftime("📆 %d-%m-%Y ⏰ %H:%M:%S")
        await call.message.answer(f"<b>✅ Sizning almashuv buyurtmangiz operatorga yuborildi, iltimos tasdiqlanishini kuting!\n\nUshbu almashuv operator tomonidan navbati bilan amalga oshiriladi va 2 daqiqadan 60 daqiqagacha davom etadi.\n\n{dt_string}</b>",reply_markup=Menu)
        await bot.send_message(ADMINS[0], f"<b>👤 foydalanuvchi {mention} quydagi almashuvni qilmoqchi👇</b>")
        await bot.send_message(ADMINS[0],msg, parse_mode="HTML")

@dp.callback_query_handler(post_callback.filter(action="cancel"), state=Qiwiu.qiwiuc)
async def cancel_post2(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>To'lov bekor qilindi.</b>",reply_markup=Menu)

@dp.message_handler(state=Qiwiu.qiwiuc)
async def enter_finshit2(message: Message, state: FSMContext):
   await message.reply("<b>👆👆👆Quyidagi Almashuvni yakunlang!\n✅ To'lov qildim yoki Bekor qilish 🚫 tugmasidan birini bosing bo'lmasa botagi boshqa tugmalar ishlamaydi🔐</b>")
