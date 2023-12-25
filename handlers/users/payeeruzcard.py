import logging
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from loader import dp, bot
from keyboards.inline.Menuin import categoryMenu, payeeruzsr
from keyboards.default.menu import Menu
from aiogram.dispatcher import FSMContext
from aiogram import types
from keyboards.inline.manage_post import confirmation_keyboard, post_callback
from states.payeeruzs import Payeerrubl
from data.config import ADMINS
import datetime
import pytz
from aiogram.dispatcher.filters import Command


@dp.message_handler(Command("otmen"),state=Payeerrubl)
async def otmea(message:
	types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>Almashuv bekor qilindi.</b>",reply_markup=Menu)
	
@dp.callback_query_handler(text="uzsbpayer")
async def Rublpayi(call: CallbackQuery):
    try:
    	id = call.message.chat.id
    	uzcardi = open(f"files/uzcard{id}.txt", "r")
    	payeeri = open(f"files/payeer{id}.txt", "r")
    	uzcardza= open("zahira/uzcardz.txt", "r")
    	uzsza = int(uzcardza.read())
    	if 5999 < uzsza:
    		await call.message.answer(f"<b>🔄Almashuv:\n\n⬆️Berish: PAYEER RUB\n⬇️Olish: UZCARD SUM*\n💳UZCARD: {uzcardi.read()}\n💸PAYEER: {payeeri.read()}</b>",reply_markup=payeeruzsr)
    		await call.message.delete()
    		await call.answer(cache_time=60)
    	else:
    		await call.answer("ℹ️ Siz tanlagan yo'nalishda almashinuv qilish imkoni hozircha yo'q",show_alert=True)
    	uzcardi.close()
    	payeeri.close()
    	uzcardza.close()
    except:
    	await call.answer("❗️Siz tanlagan yo'nalishda almashuvni amalga oshirish uchun oldin o'z hamyon raqamlaringizni  '💳 Hamyonlar' bo'limiga kiriting!", show_alert=True)

@dp.callback_query_handler(text_contains="rublpayeer")
async def rublpayee(call: CallbackQuery):
    uzcardz = open("zahira/uzcardz.txt", "r")
    payeero = open("kurs/payeerrublo.txt", "r")
    uzcardzx = int(uzcardz.read())
    payeerol = int(payeero.read())
    maksimalo = uzcardzx / payeerol
    natmak = "%.2f" % maksimalo
    await call.message.answer(f"<b>⬆️ Berish miqdorini PAYEER RUB da kiriting!\n\nMinimal  50  RUB\nMaksimal {natmak} RUB\n\nBekor qilish uchun: /otmen</b>")
    uzcardz.close()
    payeero.close()
    await call.message.delete()
    await call.answer(cache_time=60)
    await Payeerrubl.payeeruch.set()

@dp.message_handler(state=Payeerrubl.payeeruch)
async def hisobkitob(message: Message,state: FSMContext):
	try:
		payeeruch = message.text
		await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
		puli4 = int(payeeruch)
		uzcardzm = open("zahira/uzcardz.txt", "r")
		payeerom = open("kurs/payeerrublo.txt", "r")
		uzcardzxm = int(uzcardzm.read())
		payeerkm = int(payeerom.read())
		maksimalom = uzcardzxm / payeerkm
		natijamim = int(maksimalom)
		songinatijam = natijamim + 1
		uzcardzm.close()
		payeerom.close()
		if 49 < puli4 < songinatijam:
			id = message.from_user.id
			uzcardin = open(f"files/uzcard{id}.txt", "r")
			payeerin = open(f"files/payeer{id}.txt", "r")
			payeeryn = open("kurs/payeerrublo.txt", "r")
			payerinn = int(payeeryn.read())
			natijarr4n = puli4 * payerinn
			natijar4n = "%.2f" % natijarr4n
			await message.answer("P1068613774")
			msdp = f"<b>👆Ko'chirib olish uchun. Almashuvingiz muvaffaqiyatli bajarilishi uchun quyidagi harakatlarni amalga oshiring:\n1) Pastda ko'rsatilgan to'lov miqdorni\n\nP1068613774\n\n👆 PAYEER raqamiga o'tkazing;\n2) «To'lov qildim ✅» tugmasini bosing;\n3) Operator tomonidan almashuv tasdiqlanishini kuting.\n\n📥To'lov miqdori: {payeeruch} PAYEER RUB*\n\n📤Olish miqdori: {natijar4n} UZCARD SUM\n🇺🇿UZCARD: {uzcardin.read()}\n💶PAYEER: {payeerin.read()}\n\n►Ushbu almashuv operator tomonidan navbati bilan amalga oshiriladi va 2 daqiqadan 60 daqiqagacha davom etadi.</b>"
			await Payeerrubl.next()
			await message.answer(msdp,reply_markup=confirmation_keyboard)
			uzcardin.close()
			payeerin.close()
			payeeryn.close()
			await state.update_data(
				{"payeeruch": msdp}
			)
		else:
			uzcardz2 = open("zahira/uzcardz.txt", "r")
			payeerg = open("kurs/payeerrublo.txt", "r")
			uzcardzx2 = int(uzcardz2.read())
			payfok2 = int(payeerg.read())
			maksimalo2 = uzcardzx2 / payfok2
			natmak2 = "%.2f" % maksimalo2
			await message.answer(f"<b>⬆️ Berish miqdorini PAYEER RUB da kiriting!\n\nMinimal  50  RUB\nMaksimal {natmak2} RUB\n\nBekor qilish uchun: /otmen</b>")
			uzcardz2.close()
			payeerg.close()
	except:
		await message.answer("<b>❕Butun Son kiriting.</b>")


@dp.callback_query_handler(post_callback.filter(action="post"),state=Payeerrubl.payeerc)
async def confirm_post8(call: CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
        	data = await state.get_data()
        	msdp = data.get("payeeruch")
        	msg = f"<b>{msdp}</b>"
        	mention = data.get("mention")
        await state.finish()
        await call.message.edit_reply_markup()
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        pst_now = utc_now.astimezone(pytz.timezone("Asia/Tashkent"))
        dt_string = pst_now.strftime("📆 %d-%m-%Y ⏰ %H:%M:%S")
        await call.message.answer(f"<b>✅ Sizning almashuv buyurtmangiz operatorga yuborildi, iltimos tasdiqlanishini kuting!\n\nUshbu almashuv operator tomonidan navbati bilan amalga oshiriladi va 2 daqiqadan 60 daqiqagacha davom etadi.\n\n{dt_string}</b>",reply_markup=Menu)
        await bot.send_message(ADMINS[0], f"<b>👤 foydalanuvchi {mention} quydagi almashuvni qilmoqchi👇</b>")
        await bot.send_message(ADMINS[0],msg, parse_mode="HTML")

@dp.callback_query_handler(post_callback.filter(action="cancel"),state=Payeerrubl.payeerc)
async def cancel_post8(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>To'lov bekor qilindi.</b>",reply_markup=Menu)

@dp.message_handler(state=Payeerrubl.payeerc)
async def enter_finshit8(message: Message, state: FSMContext):
   await message.reply("<b>👆👆👆Quyidagi Almashuvni yakunlang!\n✅ To'lov qildim yoki Bekor qilish 🚫 tugmasidan birini bosing bo'lmasa botagi boshqa tugmalar ishlamaydi🔐</b>")