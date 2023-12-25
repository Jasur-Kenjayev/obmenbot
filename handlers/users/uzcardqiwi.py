import logging
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from loader import dp, bot
from keyboards.inline.Menuin import categoryMenu, ortga
from keyboards.default.menu import Menu
from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboards.inline.manage_post import confirmation_keyboard, post_callback
from states.newpost import NewPost
from data.config import ADMINS
import datetime
import pytz

@dp.callback_query_handler(text="menbe")
async def bekm(call: CallbackQuery):
	await call.message.answer("<b>To'lov bekor qilindi.</b>",reply_markup=Menu)
	await call.message.delete()
	await call.answer(cache_time=60)
	
	
@dp.message_handler(Command("cancel"),state=NewPost)
async def cance(message:
	types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>Almashuv bekor qilindi.</b>",reply_markup=Menu)
	
	
@dp.message_handler(text="🔄 Almashtirish")
async def almashtrish(message:
	Message):
	teld = await message.answer("📲",reply_markup=ReplyKeyboardRemove())
	await teld.delete()
	await message.answer("<b>🔄 Almashuvni tanlang\nBerish ♻️ Olish</b>",reply_markup=categoryMenu)

@dp.callback_query_handler(text="uzrub")
async def berish1(call: CallbackQuery):
    try:
    	id = call.message.chat.id
    	follow = open(f"files/uzcard{id}.txt", "r")
    	qiwi = open(f"files/qiwi{id}.txt", "r")
    	qiwiz = open("zahira/qiwiz.txt", "r")
    	qqz = int(qiwiz.read())
    	if 49 < qqz:
    		await call.message.answer(f"<b>🔄Almashuv:\n\n⬆️Berish: UZCARD SUM \n⬇️Olish: QIWI RUB* \n💳UZCARD: {follow.read()}\n💸QIWI: {qiwi.read()}</b>",reply_markup=ortga)
    		await call.message.delete()
    		await call.answer(cache_time=60)
    	else:
    		await call.answer("ℹ️ Siz tanlagan yo'nalishda almashinuv qilish imkoni hozircha yo'q",show_alert=True)
    	follow.close()
    	qiwi.close()
    	qiwiz.close()
    except:
    	await call.answer("❗️Siz tanlagan yo'nalishda almashuvni amalga oshirish uchun oldin o'z hamyon raqamlaringizni  '💳 Hamyonlar' bo'limiga kiriting!", show_alert=True)

@dp.callback_query_handler(text_contains="uzcardo")
async def uzcarqiwi(call: CallbackQuery):
    qiwif = open("kurs/qiwi.txt", "r")
    qiwiz = open("zahira/qiwiz.txt", "r")
    qiwisotishk = int(qiwif.read())
    qiwizahira = int(qiwiz.read())
    minmal = qiwisotishk * qiwizahira
    await call.message.answer(f"<b>⬆️ Berish miqdorini UZCARD SO'M da kiriting!\n\nMinimal  6000  SUM\nMaksimal {minmal} SO'M\n\nBekor qilish uchun: /cancel</b>")
    qiwif.close()
    qiwiz.close()
    await call.message.delete()
    await call.answer(cache_time=60)
    await NewPost.phone.set()

@dp.message_handler(state=NewPost.phone)
async def hisobk(message: Message,state: FSMContext):
	try:
		phone = message.text
		await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
		puli = int(phone)
		qiwifq = open("kurs/qiwi.txt", "r")
		qiwizq = open("zahira/qiwiz.txt", "r")
		qiwisotishkursi = int(qiwifq.read())
		qiwirublzahira = int(qiwizq.read())
		natijalari = qiwisotishkursi * qiwirublzahira
		maks = natijalari + 1
		qiwifq.close()
		qiwizq.close()
		if 5999 < puli < maks:
			id = message.from_user.id
			followyu = open(f"files/uzcard{id}.txt", "r")
			uzcardi = int(followyu.read())
			qiwiyu = open(f"files/qiwi{id}.txt", "r")
			qiwisi = int(qiwiyu.read())
			qiwifyu = open("kurs/qiwi.txt", "r")
			qiwifs = int(qiwifyu.read())
			natijar = puli / qiwifs
			natijar1 = "%.2f" % natijar
		
			await message.answer("8600332962820019")
			msd = f"<b>KENJAYEV JASUR 👆Ko'chirib olish uchun. Almashuvingiz muvaffaqiyatli bajarilishi uchun quyidagi harakatlarni amalga oshiring:\n1) Pastda ko'rsatilgan to'lov miqdorni\n\n8600332962820019\n\n👆karta raqamiga o'tkazing;\n2) «To'lov qildim ✅» tugmasini bosing;\n3) Operator tomonidan almashuv tasdiqlanishini kuting.\n\n📥To'lov miqdori: {phone} UZCARD SUM\n\n📤Olish miqdori: {natijar1} QIWI RUB*\n🇺🇿UZCARD: {uzcardi}\n🇷🇺QIWI: {qiwisi}\n\n►PAYME, CLICK , APELSIN - to'lov tizimlaridan birida to'lov qilsangiz to'lovingiz tezroq bajariladi\n►Ushbu almashuv operator tomonidan navbati bilan amalga oshiriladi va 2 daqiqadan 60 daqiqagacha davom etadi.</b>"
			await NewPost.next()
			await message.answer(msd,reply_markup=confirmation_keyboard)
			qiwiyu.close()
			followyu.close()
			qiwifyu.close()
			await state.update_data(
				{"phone": msd}
			)
		else:
			qiwifqw = open("kurs/qiwi.txt", "r")
			qiwizqw = open("zahira/qiwiz.txt", "r")
			qiwisotishkursiqw = int(qiwifqw.read())
			qiwirublzahiraqw = int(qiwizqw.read())
			natijalarqw = qiwisotishkursiqw * qiwirublzahiraqw
			await message.answer(f"<b>Berish miqdorini UZS'da kiriting\nMinimal: 6000 UZS\nMaksimal: {natijalarqw} UZS\n\nBekor qilish uchun: /cancel</b>")
			qiwifqw.close()
			qiwizqw.close()
	except:
		await message.answer("<b>❕Butun Son kiriting.</b>")
	
@dp.callback_query_handler(post_callback.filter(action="post"), state=NewPost.Confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
        	data = await state.get_data()
        	msd = data.get("phone")
        	msg = f"<b>{msd}</b>"
        	mention = data.get("mention")
        await state.finish()
        await call.message.edit_reply_markup()
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        pst_now = utc_now.astimezone(pytz.timezone("Asia/Tashkent"))
        dt_string = pst_now.strftime("📆 %d-%m-%Y ⏰ %H:%M:%S")
        await call.message.answer(f"<b>✅ Sizning almashuv buyurtmangiz operatorga yuborildi, iltimos tasdiqlanishini kuting!\n\nUshbu almashuv operator tomonidan navbati bilan amalga oshiriladi va 2 daqiqadan 60 daqiqagacha davom etadi.\n\n{dt_string}</b>",reply_markup=Menu)
        await bot.send_message(ADMINS[0], f"<b>👤 foydalanuvchi {mention} quydagi almashuvni qilmoqchi👇</b>")
        await bot.send_message(ADMINS[0],msg, parse_mode="HTML")

@dp.callback_query_handler(post_callback.filter(action="cancel"), state=NewPost.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>To'lov bekor qilindi.</b>",reply_markup=Menu)

@dp.message_handler(state=NewPost.Confirm)
async def enter_finshit(message: Message, state: FSMContext):
   await message.reply("<b>👆👆👆Quyidagi Almashuvni yakunlang!\n✅ To'lov qildim yoki Bekor qilish 🚫 tugmasidan birini bosing bo'lmasa botagi boshqa tugmalar ishlamaydi🔐</b>")