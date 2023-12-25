import logging
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from loader import dp, bot
from keyboards.inline.Menuin import categoryMenu, payusduzcard
from keyboards.default.menu import Menu
from aiogram.dispatcher import FSMContext
from aiogram import types
from keyboards.inline.manage_post import confirmation_keyboard, post_callback
from states.pusdstate import UsdUzs
from data.config import ADMINS
import datetime
import pytz
from aiogram.dispatcher.filters import Command

@dp.message_handler(Command("cancele"),state=UsdUzs)
async def cancele(message:
	types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>Almashuv bekor qilindi.</b>",reply_markup=Menu)
	
@dp.callback_query_handler(text="PusDuz")
async def PusDuz(call: CallbackQuery):
    try:
    	id = call.message.chat.id
    	iduzixo = open(f"files/uzcard{id}.txt", "r")
    	payeerixo = open(f"files/payeer{id}.txt", "r")
    	uzcardzidxo = open("zahira/uzcardz.txt", "r")
    	uzszxo = int(uzcardzidxo.read())
    	if 15000 < uzszxo:
    		await call.message.answer(f"<b>🔄Almashuv:\n\n⬆️Berish: PAYEER USD\n⬇️Olish: UZCARD SUM*\n💳UZCARD: {iduzixo.read()}\n💸PAYEER: {payeerixo.read()}</b>",reply_markup=payusduzcard)
    		await call.message.delete()
    		await call.answer(cache_time=60)
    	else:
    		await call.answer("ℹ️ Siz tanlagan yo'nalishda almashinuv qilish imkoni hozircha yo'q",show_alert=True)
    	iduzixo.close()
    	uzcardzidxo.close()
    	payeerixo.close()
    except:
    	await call.answer("❗️Siz tanlagan yo'nalishda almashuvni amalga oshirish uchun oldin o'z hamyon raqamlaringizni  '💳 Hamyonlar' bo'limiga kiriting!", show_alert=True)

@dp.callback_query_handler(text_contains="payUsdi")
async def payUsdi1(call: CallbackQuery):
    zuzcardxo = open("zahira/uzcardz.txt", "r")
    kpayusd = open("kurs/payeero.txt", "r")
    zahirauz = int(zuzcardxo.read())
    usdkursolish = int(kpayusd.read())
    uzvausd = zahirauz / usdkursolish
    uzvausds = "%.2f" % uzvausd
    await call.message.answer(f"<b>⬆️ Berish miqdorini PAYEER USD da kiriting!\n\nMinimal 1 USD\nMaksimal {uzvausds} USD\n\nBekor qilish uchun: /cancele</b>")
    zuzcardxo.close()
    kpayusd.close()
    await call.message.delete()
    await call.answer(cache_time=60)
    await UsdUzs.usduzc.set()

@dp.message_handler(state=UsdUzs.usduzc)
async def hisobusd2(message: Message,state: FSMContext):
	try:
		usduzc = message.text
		await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
		usdpul = float(usduzc)
		zauzcardxo = open("zahira/uzcardz.txt", "r")
		payusdkuxo = open("kurs/payeero.txt", "r")
		uzcardixo = int(zauzcardxo.read())
		usduzsxo = int(payusdkuxo.read())
		hisobvakitob = uzcardixo / usduzsxo
		kitobhisobs = hisobvakitob
		zauzcardxo.close()
		payusdkuxo.close()
		if 0.99 < usdpul < kitobhisobs:
			id = message.from_user.id
			uzplast = open(f"files/uzcard{id}.txt", "r")
			payeerixo = open(f"files/payeer{id}.txt", "r")
			payusdkusio = open("kurs/payeero.txt", "r")
			paysio = float(payusdkusio.read())
			natijasiv = usdpul * paysio
			natijasif = "%.2f" % natijasiv
			await message.answer("P1068613774")
			msdsi = f"<b>👆Ko'chirib olish uchun. Almashuvingiz muvaffaqiyatli bajarilishi uchun quyidagi harakatlarni amalga oshiring:\n1) Pastda ko'rsatilgan to'lov miqdorni\n\nP1068613774\n\n👆PAYEER raqamiga o'tkazing;\n2) «To'lov qildim ✅» tugmasini bosing;\n3) Operator tomonidan almashuv tasdiqlanishini kuting.\n\n📥To'lov miqdori: {usdpul} PAYEER USD\n\n📤Olish miqdori: {natijasif} UZCARD SUM*\n🇺🇿UZCARD: {uzplast.read()}\n💶PAYEER: {payeerixo.read()}\n\n►Ushbu almashuv operator tomonidan navbati bilan amalga oshiriladi va 2 daqiqadan 60 daqiqagacha davom etadi.</b>"
			await UsdUzs.next()
			await message.answer(msdsi,reply_markup=confirmation_keyboard)
			uzplast.close()
			payeerixo.close()
			payusdkusio.close()
			await state.update_data(
				{"usduzc": msdsi}
			)
		else:
			uzcardti = open("zahira/uzcardz.txt", "r")
			payerti = open("kurs/payeero.txt", "r")
			uzszahirati = int(uzcardti.read())
			pusdolishkurs = int(payerti.read())
			uzvausdti = uzszahirati / pusdolishkurs
			uzvausdsti = "%.2f" % uzvausdti
			await message.answer(f"<b>⬆️ Berish miqdorini PAYEER USD da kiriting!\n\nMinimal  1 USD\nMaksimal {uzvausdsti} USD\n\nBekor qilish uchun: /cancele</b>")
			uzcardti.close()
			payerti.close()
	except:
		await message.answer("<b>❕Son kiriting.</b>")
		
@dp.callback_query_handler(post_callback.filter(action="post"),state=UsdUzs.usduzcaC)
async def confirm_post5(call: CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
        	data = await state.get_data()
        	msdsi = data.get("usduzc")
        	msgsi = f"<b>{msdsi}</b>"
        	mention = data.get("mention")
        await state.finish()
        await call.message.edit_reply_markup()
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        pst_now = utc_now.astimezone(pytz.timezone("Asia/Tashkent"))
        dt_string = pst_now.strftime("📆 %d-%m-%Y ⏰ %H:%M:%S")
        await call.message.answer(f"<b>✅ Sizning almashuv buyurtmangiz operatorga yuborildi, iltimos tasdiqlanishini kuting!\n\nUshbu almashuv operator tomonidan navbati bilan amalga oshiriladi va 2 daqiqadan 60 daqiqagacha davom etadi.\n\n{dt_string}</b>",reply_markup=Menu)
        await bot.send_message(ADMINS[0], f"<b>👤 foydalanuvchi {mention} quydagi almashuvni qilmoqchi👇</b>")
        await bot.send_message(ADMINS[0],msgsi, parse_mode="HTML")

@dp.callback_query_handler(post_callback.filter(action="cancel"), state=UsdUzs.usduzcaC)
async def cancel_post5(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("<b>To'lov bekor qilindi.</b>",reply_markup=Menu)

@dp.message_handler(state=UsdUzs.usduzcaC)
async def enter_finshit5(message: Message, state: FSMContext):
   await message.reply("<b>👆👆👆Quyidagi Almashuvni yakunlang!\n✅ To'lov qildim yoki Bekor qilish 🚫 tugmasidan birini bosing bo'lmasa botagi boshqa tugmalar ishlamaydi🔐</b>")