import logging
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from loader import dp, bot
from keyboards.inline.Menuin import categoryMenu, uzcardpayeerb
from keyboards.default.menu import Menu
from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboards.inline.manage_post import confirmation_keyboard, post_callback
from states.payeerstate import Payeerus
from data.config import ADMINS
import datetime
import pytz

@dp.message_handler(Command("otmena"),state=Payeerus)
async def cancep(message:
	types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>Almashuv bekor qilindi.</b>",reply_markup=Menu)

@dp.callback_query_handler(text="payuzsu")
async def uzspayeerru(call: CallbackQuery):
	try:
	    id = call.message.chat.id
	    follow = open(f"files/uzcard{id}.txt", "r")
	    payeer = open(f"files/payeer{id}.txt", "r")
	    payeerz = open("zahira/payeerz.txt", "r")
	    pay = int(payeerz.read())
	    if 49 < pay:
	    	await call.message.answer(f"<b>🔄Almashuv:\n\n⬆️Berish: UZCARD SUM \n⬇️Olish: PAYEER RUB* \n💳UZCARD: {follow.read()}\n💸PAYEER: {payeer.read()}</b>",reply_markup=uzcardpayeerb)
	    	await call.message.delete()
	    	await call.answer(cache_time=60)
	    else:
	    	await call.answer("ℹ️ Siz tanlagan yo'nalishda almashinuv qilish imkoni hozircha yo'q",show_alert=True)
	    follow.close()
	    payeer.close()
	    payeerz.close()
	except:
		await call.answer("❗️Siz tanlagan yo'nalishda almashuvni amalga oshirish uchun oldin o'z hamyon raqamlaringizni  '💳 Hamyonlar' bo'limiga kiriting!", show_alert=True)

@dp.callback_query_handler(text_contains="uzbekpayer")
async def uzpayree(call: CallbackQuery):
    payerrubf = open("kurs/payeerrubl.txt", "r")
    payeerzq = open("zahira/payeerz.txt", "r")
    paysotishk = int(payerrubf.read())
    payzahira = int(payeerzq.read())
    minmal3 = paysotishk * payzahira
    
    await call.message.answer(f"<b>⬆️ Berish miqdorini UZCARD SO'M da kiriting!\n\nMinimal  6000  SUM\nMaksimal {minmal3} SO'M\n\nBekor qilish uchun: /otmena</b>")
    payerrubf.close()
    payeerzq.close()
    await call.message.delete()
    await call.answer(cache_time=60)
    await Payeerus.payeeri.set()

@dp.message_handler(state=Payeerus.payeeri)
async def hisoblash3(message: Message,state: FSMContext):
	try:
		payeeri = message.text
		await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
		kiritganpuli = int(payeeri)
		payerrubff = open("kurs/payeerrubl.txt", "r")
		payeerzz = open("zahira/payeerz.txt", "r")
		paysotishkk = int(payerrubff.read())
		payzahiraa = int(payeerzz.read())
		minmali = paysotishkk * payzahiraa
		macsi = minmali + 1
		payerrubff.close()
		payeerzz.close()
		if 5999 < kiritganpuli < macsi:
			id = message.from_user.id
			payeerh = open(f"files/payeer{id}.txt", "r")
			followh = open(f"files/uzcard{id}.txt", "r")
			payerrubh = open("kurs/payeerrubl.txt", "r")
			payifs = int(payerrubh.read())
			natijarsi = kiritganpuli / payifs
			natijarh = "%.2f" % natijarsi
			await message.answer("9860080181620333")
			msdk = f"<b>KENJAYEV JASUR 👆Ko'chirib olish uchun. Almashuvingiz muvaffaqiyatli bajarilishi uchun quyidagi harakatlarni amalga oshiring:\n1) Pastda ko'rsatilgan to'lov miqdorni\n\n9860080181620333\n\n👆karta raqamiga o'tkazing;\n2) «To'lov qildim ✅» tugmasini bosing;\n3) Operator tomonidan almashuv tasdiqlanishini kuting.\n\n📥To'lov miqdori: {payeeri} UZCARD SUM\n\n📤Olish miqdori: {natijarh} PAYEER RUB*\n🇺🇿UZCARD: {followh.read()}\n💶PAYEER: {payeerh.read()}\n\n►PAYME, CLICK , APELSIN - to'lov tizimlaridan birida to'lov qilsangiz to'lovingiz tezroq bajariladi\n►Ushbu almashuv operator tomonidan navbati bilan amalga oshiriladi va 2 daqiqadan 60 daqiqagacha davom etadi.</b>"
			await Payeerus.next()
			await message.answer(msdk,reply_markup=confirmation_keyboard)
			followh.close()
			payeerh.close()
			payerrubh.close()
			await state.update_data(
				{"payeeri": msdk}
			)
		else:
			payerrubfff = open("kurs/payeerrubl.txt", "r")
			payeerzzz = open("zahira/payeerz.txt", "r")
			paysotishkkk = int(payerrubfff.read())
			payzahiraaa = int(payeerzzz.read())
			minmall = paysotishkkk * payzahiraaa
			natmakkk = "%.2f" % minmall
			await message.answer(f"<b>⬆️ Berish miqdorini UZCARD SO'M da kiriting!\n\nMinimal  6000  SUM\nMaksimal {natmakkk} SO'M\n\nBekor qilish uchun: /otmena</b>")
			payerrubfff.close()
			payeerzzz.close()
	except:
		await message.answer("<b>❕Butun Son kiriting.</b>")
	
@dp.callback_query_handler(post_callback.filter(action="post"), state=Payeerus.payeerC)
async def confirm_post9(call: CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
        	data = await state.get_data()
        	msdk = data.get("payeeri")
        	msgo = f"<b>{msdk}</b>"
        	mention = data.get("mention")
        await state.finish()
        await call.message.edit_reply_markup()
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        pst_now = utc_now.astimezone(pytz.timezone("Asia/Tashkent"))
        dt_string = pst_now.strftime("📆 %d-%m-%Y ⏰ %H:%M:%S")
        await call.message.answer(f"<b>✅ Sizning almashuv buyurtmangiz operatorga yuborildi, iltimos tasdiqlanishini kuting!\n\nUshbu almashuv operator tomonidan navbati bilan amalga oshiriladi va 2 daqiqadan 60 daqiqagacha davom etadi.\n\n{dt_string}</b>",reply_markup=Menu)
        await bot.send_message(ADMINS[0], f"<b>👤 foydalanuvchi {mention} quydagi almashuvni qilmoqchi👇</b>")
        await bot.send_message(ADMINS[0],msgo, parse_mode="HTML")

@dp.callback_query_handler(post_callback.filter(action="cancel"), state=Payeerus.payeerC)
async def cancel_post9(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>To'lov bekor qilindi.</b>",reply_markup=Menu)

@dp.message_handler(state=Payeerus.payeerC)
async def enter_finshit9(message: Message, state: FSMContext):
   await message.reply("<b>👆👆👆Quyidagi Almashuvni yakunlang!\n✅ To'lov qildim yoki Bekor qilish 🚫 tugmasidan birini bosing bo'lmasa botagi boshqa tugmalar ishlamaydi🔐</b>")
