import logging
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from loader import dp, bot
from keyboards.inline.Menuin import categoryMenu, uzcardpayeerusd
from keyboards.default.menu import Menu
from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboards.inline.manage_post import confirmation_keyboard, post_callback
from states.payusds import PayUsd
from data.config import ADMINS
import datetime
import pytz
	
	
@dp.message_handler(Command("orqaga"),state=PayUsd)
async def orqaga(message:
	types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>Almashuv bekor qilindi.</b>",reply_markup=Menu)
	

@dp.callback_query_handler(text="PayerUsD")
async def PayerUsD(call: CallbackQuery):
    try:
    	id = call.message.chat.id
    	uzcardi = open(f"files/uzcard{id}.txt", "r")
    	payeeri = open(f"files/payeer{id}.txt", "r")
    	usdz = open("zahira/payeerusd.txt", "r")
    	pusd = int(usdz.read())
    	if 1 < pusd:
    		await call.message.answer(f"<b>🔄Almashuv:\n\n⬆️Berish: UZCARD SUM \n⬇️Olish: PAYEER USD* \n💳UZCARD: {uzcardi.read()}\n💸PAYEER: {payeeri.read()}</b>",reply_markup=uzcardpayeerusd)
    		await call.message.delete()
    		await call.answer(cache_time=60)
    	else:
    		await call.answer("ℹ️ Siz tanlagan yo'nalishda almashinuv qilish imkoni hozircha yo'q",show_alert=True)
    	uzcardi.close()
    	payeeri.close()
    	usdz.close()
    except:
    	await call.answer("❗️Siz tanlagan yo'nalishda almashuvni amalga oshirish uchun oldin o'z hamyon raqamlaringizni  '💳 Hamyonlar' bo'limiga kiriting!", show_alert=True)

@dp.callback_query_handler(text_contains="Dastusdp")
async def Dastusd(call: CallbackQuery):
    payerf = open("kurs/payeer.txt", "r")
    usdza = open("zahira/payeerusd.txt", "r")
    paysotishk = int(payerf.read())
    usdzahira = int(usdza.read())
    minmals = paysotishk * usdzahira
    
    await call.message.answer(f"<b>⬆️ Berish miqdorini UZCARD SO'M da kiriting!\n\nMinimal 11500  SUM\nMaksimal {minmals} SO'M\n\nBekor qilish uchun: /orqaga</b>")
    payerf.close()
    usdza.close()
    await call.message.delete()
    await call.answer(cache_time=60)
    await PayUsd.payeusd.set()

@dp.message_handler(state=PayUsd.payeusd)
async def hisobusd(message: Message,state: FSMContext):
	try:
		payeusd = message.text
		await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
		puliusd = int(payeusd)
		payerff = open("kurs/payeer.txt", "r")
		usdzaa = open("zahira/payeerusd.txt", "r")
		usdsotishkursi = int(payerff.read())
		usdzahira = int(usdzaa.read())
		natijalariu = usdsotishkursi * usdzahira
		maks = natijalariu + 1
		payerff.close()
		usdzaa.close()
		if 11499 < puliusd < maks:
			id = message.from_user.id
			uzcardr = open(f"files/uzcard{id}.txt", "r")
			payeerir= open(f"files/payeer{id}.txt", "r")
			payerfff = open("kurs/payeer.txt", "r")
			payerint = int(payerfff.read())
			natija = puliusd / payerint
			natijasi = "%.2f" % natija
		
			await message.answer("9860080181620333")
			msdusd = f"<b>KENJAYEV JASUR 👆Ko'chirib olish uchun. Almashuvingiz muvaffaqiyatli bajarilishi uchun quyidagi harakatlarni amalga oshiring:\n1) Pastda ko'rsatilgan to'lov miqdorni\n\n9860080181620333\n\n👆karta raqamiga o'tkazing;\n2) «To'lov qildim ✅» tugmasini bosing;\n3) Operator tomonidan almashuv tasdiqlanishini kuting.\n\n📥To'lov miqdori: {puliusd} UZCARD SUM\n\n📤Olish miqdori: {natijasi} PAYEER USD*\n💳UZCARD: {uzcardr.read()}\n💵PAYEER: {payeerir.read()}\n\n►PAYME, CLICK , APELSIN - to'lov tizimlaridan birida to'lov qilsangiz to'lovingiz tezroq bajariladi\n►Ushbu almashuv operator tomonidan navbati bilan amalga oshiriladi va 2 daqiqadan 60 daqiqagacha davom etadi.</b>"
			await PayUsd.next()
			await message.answer(msdusd,reply_markup=confirmation_keyboard)
			uzcardr.close()
			payeerir.close()
			payerfff.close()
			await state.update_data(
				{"payeusd": msdusd}
			)
		else:
			pyusd = open("kurs/payeer.txt", "r")
			pyzahira = open("zahira/payeerusd.txt", "r")
			pusdsotishk = int(pyusd.read())
			pusdzahira = int(pyzahira.read())
			natijalari = pusdsotishk * pusdzahira
			await message.answer(f"<b>Berish miqdorini UZS'da kiriting\nMinimal: 11500 UZS\nMaksimal: {natijalari} UZS\n\nBekor qilish uchun: /orqaga</b>")
			pyusd.close()
			pyzahira.close()
	except:
		await message.answer("<b>❕Butun Son kiriting.</b>")
	
@dp.callback_query_handler(post_callback.filter(action="post"), state=PayUsd.payeusdC)
async def confirm_post7(call: CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
        	data = await state.get_data()
        	msdusd = data.get("payeusd")
        	msg = f"<b>{msdusd}</b>"
        	mention = data.get("mention")
        await state.finish()
        await call.message.edit_reply_markup()
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        pst_now = utc_now.astimezone(pytz.timezone("Asia/Tashkent"))
        dt_string = pst_now.strftime("📆 %d-%m-%Y ⏰ %H:%M:%S")
        await call.message.answer(f"<b>✅ Sizning almashuv buyurtmangiz operatorga yuborildi, iltimos tasdiqlanishini kuting!\n\nUshbu almashuv operator tomonidan navbati bilan amalga oshiriladi va 2 daqiqadan 60 daqiqagacha davom etadi.\n\n{dt_string}</b>",reply_markup=Menu)
        await bot.send_message(ADMINS[0], f"<b>👤 foydalanuvchi {mention} quydagi almashuvni qilmoqchi👇</b>")
        await bot.send_message(ADMINS[0],msg, parse_mode="HTML")

@dp.callback_query_handler(post_callback.filter(action="cancel"), state=PayUsd.payeusdC)
async def cancel_post7(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>To'lov bekor qilindi.</b>",reply_markup=Menu)

@dp.message_handler(state=PayUsd.payeusdC)
async def enter_finshit7(message: Message, state: FSMContext):
   await message.reply("<b>👆👆👆Quyidagi Almashuvni yakunlang!\n✅ To'lov qildim yoki Bekor qilish 🚫 tugmasidan birini bosing bo'lmasa botagi boshqa tugmalar ishlamaydi🔐</b>")
