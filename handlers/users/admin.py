import asyncio
from aiogram.dispatcher import FSMContext
from keyboards.default.menu import Menu
from states.stett import PersonalData
from aiogram import types
from keyboards.default.adminKeyboard import panel, bekor1, zahirakurs, zahiram, sotisholish, olishkur, bekor2, bekor, zahiraw, bekor3
from data.config import ADMINS
from loader import dp, db, bot
import datetime
import pytz
from aiogram.types import ParseMode, Message

@dp.message_handler(text= "Orqaga🏠",state=PersonalData,user_id=ADMINS)
async def enter_uya(message:
	types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>🤖Orqaga Muvafaqiyatli qaytdingiz✅</b>",reply_markup=zahiram)

@dp.message_handler(text= "*⃣ Orqaga",state=PersonalData,user_id=ADMINS)
async def enter_uya3(message:
	types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>🤖Orqaga Muvafaqiyatli qaytdingiz✅</b>",reply_markup=zahiraw)
	

@dp.message_handler(text= "🏠 Orqaga",state=PersonalData,user_id=ADMINS)
async def enter_uya2(message:
	types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>🤖Orqaga Muvafaqiyatli qaytdingiz✅</b>",reply_markup=olishkur)
	
@dp.message_handler(text= "Orqaga🔜",state=PersonalData.adss,user_id=ADMINS)
async def enter_exiit(message:
	types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>🤖Orqaga Muvafaqiyatli qaytdingiz✅</b>",reply_markup=panel)
	
@dp.message_handler(text = "/panel", user_id=ADMINS)
async def admin_panel(message:
	types.Message):
		await message.answer(f"*🤖Assalomu Alaykum Xurmatli {message.from_user.full_name}\n\n👤Admin Panelga Xush Kelibsiz\n🎗Kerakli Tugmani Tanlang✅*",parse_mode=ParseMode.MARKDOWN,reply_markup=panel)
		
@dp.message_handler(text="👤 ALL USERS", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    await message.answer(users,parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(text="📨 SEND MSG", user_id=ADMINS)
async def enter_obm(message: types.Message):
    await message.answer("<b>🤖 Ushbu bo'lim orqali botdagi Barcha Foydalanuvchilarga 📬 Xabar Yuborishingiz Mumkun✅</b>",reply_markup=bekor)
    await PersonalData.adss.set()


@dp.message_handler(user_id = ADMINS,state=PersonalData.adss,content_types=types.ContentType.ANY)
async def send_message_users(message:
	types.Message,state: FSMContext):
	await state.finish()
	await message.answer("<i>🗞 Xabar Yuborilmoqda....</i>")
	n = 0
	for i in db.get_users_id():
		user_id = i[0]
		try:
			await message.send_copy(chat_id = user_id)
			n+=1
		except:
			pass
		await asyncio.sleep(0.3)
	await message.answer(f"<b>📲 Xabar {n} ta foydalanuvchiga muafaqiyatli yuborildi ✅</b>",reply_markup=panel)

@dp.message_handler(text='📈 BOT STATISTIKASI',user_id=ADMINS)
async def send_usd(message:
	types.Message):
		utc_now = pytz.utc.localize(datetime.datetime.utcnow())
		pst_now = utc_now.astimezone(pytz.timezone("Asia/Tashkent"))
		dt_string = pst_now.strftime("<i>%d.%m.%Y-YIL</i>\n<b>⏰ Soat 👉</b> <i>%H:%M:%S</i>")
		count = db.count_users()[0]
		msg = f"<b>🤖 BOT STATISTIKASI 📊\n\n📆 Bugun 👉</b> {dt_string}\n👥 <b>Barcha Obunachilar =</b> <i>{count} ta</i>\n\n<b>✅ @obmennbot</b>"
		photo_id = "AgACAgIAAxkBAAIOg2JDP0PkfcagKeCjxcA-dx-kknlIAAJ3ujEbdN8YSuIbtGJTbfixAQADAgADeAADIwQ"
		await message.answer_photo(photo_id,caption=msg)
		  
@dp.message_handler(text="🔚MENU🔜",user_id=ADMINS)
async def boshmenu(message:
	types.Message):
		await message.answer(f"*🤖Xurmatli {message.from_user.full_name} Bosh Menudasiz✅*",parse_mode=ParseMode.MARKDOWN,reply_markup=Menu)
		
		
@dp.message_handler(text="📊 Kurs 💰Zahira",user_id=ADMINS)
async def zahira(message:
	types.Message):
		await message.answer(f"<b>ℹ️ Quyidagi Menudan Birini Tanlang👇</b>",reply_markup=zahirakurs)

@dp.message_handler(text="📉 Kurs",user_id=ADMINS)
async def kursz(message:
	types.Message):
		await message.answer("<b>ℹ️ Marhamat Kerakli Menuni Tanlang!</b>",reply_markup=sotisholish)

@dp.message_handler(text="↗️ Sotish Kursi",user_id=ADMINS)
async def sotish(message:
	types.Message):
		await message.answer("<b>ℹ️ Marhamat Kerakli Menuni Tanlang!</b>",reply_markup=zahiram)
		
@dp.message_handler(text="💎 Qiwi Rubl", user_id=ADMINS)
async def kurs_qiwi(message: types.Message):
    await message.answer("<b>💎 QIWI Rubl Kursni Kiriting👇</b>",reply_markup=bekor1)
    await PersonalData.qiwik.set()
    
@dp.message_handler(state=PersonalData.qiwik)
async def qiwi_kurs(message: types.Message, state: FSMContext):
    Qiwik = message.text
    qiwif = open("kurs/qiwi.txt", "w")
    qiwif.write(Qiwik)
    qiwif.close()
    await message.answer("<b>📊Kurs O'zgartirildi✅</b>",reply_markup=zahiram)
    await state.finish()

@dp.message_handler(text="💵 Payeer USD", user_id=ADMINS)
async def kurs_payer(message: types.Message):
    await message.answer("<b>💵 Payeer USD Kursni Kiriting👇</b>",reply_markup=bekor1)
    await PersonalData.payeerk.set()
    
@dp.message_handler(state=PersonalData.payeerk)
async def payer_kurs(message: types.Message, state: FSMContext):
    payerk = message.text
    payerf = open("kurs/payeer.txt", "w")
    payerf.write(payerk)
    payerf.close()
    await message.answer("<b>📊Kurs O'zgartirildi✅</b>",reply_markup=zahiram)
    await state.finish()

@dp.message_handler(text="💶 Payeer Rubl", user_id=ADMINS)
async def kurs_payerrub(message: types.Message):
    await message.answer("<b>💶 Payeer Rubl Kursni Kiriting👇</b>",reply_markup=bekor1)
    await PersonalData.payeerrubk.set()
    
@dp.message_handler(state=PersonalData.payeerrubk)
async def payerrub_kurs(message: types.Message, state: FSMContext):
    payerrubk = message.text
    payerrubf = open("kurs/payeerrubl.txt", "w")
    payerrubf.write(payerrubk)
    payerrubf.close()
    await message.answer("<b>📊Kurs O'zgartirildi✅</b>",reply_markup=zahiram)
    await state.finish()

@dp.message_handler(text= "↩️ Orqaga",user_id=ADMINS)
async def stetbre(message:
	types.Message):
	await message.answer("<b>🤖Orqaga Muvafaqiyatli qaytdingiz✅</b>",reply_markup=sotisholish)

@dp.message_handler(text= "Orqaga ⤴️",user_id=ADMINS)
async def olishor(message:
	types.Message):
	await message.answer("<b>🤖Orqaga Muvafaqiyatli qaytdingiz✅</b>",reply_markup=sotisholish)
	
@dp.message_handler(text= "◀️ Panel",user_id=ADMINS)
async def cpanel(message:
	types.Message):
	await message.answer("<b>🤖Orqaga Muvafaqiyatli qaytdingiz✅</b>",reply_markup=panel)
	
@dp.message_handler(text="↘️ Olish Kursi",user_id=ADMINS)
async def olish(message:
	types.Message):
		await message.answer("<b>ℹ️ Marhamat Kerakli Menuni Tanlang!</b>",reply_markup=olishkur)

@dp.message_handler(text="🪙 Qiwi Rubl", user_id=ADMINS)
async def kurs_qiwio(message: types.Message):
    await message.answer("<b>💎 QIWI Rubl Kursni Kiriting👇</b>",reply_markup=bekor2)
    await PersonalData.qiwio.set()
    
@dp.message_handler(state=PersonalData.qiwio)
async def qiwi_kurso(message: types.Message, state: FSMContext):
    Qiwiko = message.text
    qiwifo = open("kurs/qiwio.txt", "w")
    qiwifo.write(Qiwiko)
    qiwifo.close()
    await message.answer("<b>📊Kurs O'zgartirildi✅</b>",reply_markup=olishkur)
    await state.finish()

@dp.message_handler(text="💰Payeer USD", user_id=ADMINS)
async def kurs_payero(message: types.Message):
    await message.answer("<b>💵 Payeer USD Kursni Kiriting👇</b>",reply_markup=bekor2)
    await PersonalData.payero.set()
    
@dp.message_handler(state=PersonalData.payero)
async def payer_kurso(message: types.Message, state: FSMContext):
    payerko = message.text
    payerfo = open("kurs/payeero.txt", "w")
    payerfo.write(payerko)
    payerfo.close()
    await message.answer("<b>📊Kurs O'zgartirildi✅</b>",reply_markup=olishkur)
    await state.finish()

@dp.message_handler(text="💷 Payeer Rubl", user_id=ADMINS)
async def kurs_payerrubo(message: types.Message):
    await message.answer("<b>💶 Payeer Rubl Kursni Kiriting👇</b>",reply_markup=bekor2)
    await PersonalData.payerro.set()
    
@dp.message_handler(state=PersonalData.payerro)
async def payerrub_kurso(message: types.Message, state: FSMContext):
    payerrubko = message.text
    payerrubfo = open("kurs/payeerrublo.txt", "w")
    payerrubfo.write(payerrubko)
    payerrubfo.close()
    await message.answer("<b>📊Kurs O'zgartirildi✅</b>",reply_markup=olishkur)
    await state.finish()
	
@dp.message_handler(text= "Ortga ▶️",user_id=ADMINS)
async def cancr(message:
	types.Message):
	await message.answer("<b>🤖Orqaga Muvafaqiyatli qaytdingiz✅</b>",reply_markup=zahirakurs)

@dp.message_handler(text="💸 Zahira",user_id=ADMINS)
async def olish(message:
	types.Message):
		await message.answer("<b>ℹ️ Marhamat Kerakli Menuni Tanlang!</b>",reply_markup=zahiraw)

@dp.message_handler(text="2⃣ UZCARD", user_id=ADMINS)
async def uzcard_z(message: types.Message):
    await message.answer("<b>💳 UZCARD Kartangizdagi Barcha Pul Miqdorini Kiriting!</b>",reply_markup=bekor3)
    await PersonalData.uzcardz.set()
    
@dp.message_handler(state=PersonalData.uzcardz)
async def z_uzcard(message: types.Message, state: FSMContext):
    uzcardm = message.text
    uzcardz = open("zahira/uzcardz.txt", "w")
    uzcardz.write(uzcardm)
    uzcardz.close()
    await message.answer("<b>💸 Pul Miqdori Kiritildi✅</b>",reply_markup=zahiraw)
    await state.finish()

@dp.message_handler(text="3⃣ QIWI RUB", user_id=ADMINS)
async def qiwi_z(message: types.Message):
    await message.answer("<b>💳 QIWI hamyoningiz dagi Barcha Pul Miqdorini Kiriting!</b>",reply_markup=bekor3)
    await PersonalData.qiwiz.set()
    
@dp.message_handler(state=PersonalData.qiwiz)
async def z_qiwi(message: types.Message, state: FSMContext):
    qiwim = message.text
    qiwiz = open("zahira/qiwiz.txt", "w")
    qiwiz.write(qiwim)
    qiwiz.close()
    await message.answer("<b>💸 Pul Miqdori Kiritildi✅</b>",reply_markup=zahiraw)
    await state.finish()

@dp.message_handler(text="4⃣ PAYEER RUB", user_id=ADMINS)
async def payeer_z(message: types.Message):
    await message.answer("<b>💳 PAYEER RUB hamyoningiz dagi Barcha Pul Miqdorini Kiriting!</b>",reply_markup=bekor3)
    await PersonalData.payeerz.set()
    
@dp.message_handler(state=PersonalData.payeerz)
async def z_payeer(message: types.Message, state: FSMContext):
    payeerm = message.text
    payeerz = open("zahira/payeerz.txt", "w")
    payeerz.write(payeerm)
    payeerz.close()
    await message.answer("<b>💸 Pul Miqdori Kiritildi✅</b>",reply_markup=zahiraw)
    await state.finish()

@dp.message_handler(text="5⃣ PAYEER USD", user_id=ADMINS)
async def payusd_z(message: types.Message):
    await message.answer("<b>💳 PAYEER USD hamyoningiz dagi Barcha Pul Miqdorini Kiriting!</b>",reply_markup=bekor3)
    await PersonalData.payusdd.set()
    
@dp.message_handler(state=PersonalData.payusdd)
async def z_payu(message: types.Message, state: FSMContext):
    usdm = message.text
    usdz = open("zahira/payeerusd.txt", "w")
    usdz.write(usdm)
    usdz.close()
    await message.answer("<b>💸 Pul Miqdori Kiritildi✅</b>",reply_markup=zahiraw)
    await state.finish()

@dp.message_handler(text= "⤵️ Orqaga",user_id=ADMINS)
async def zorqa(message:
	types.Message):
	await message.answer("<b>🤖Orqaga Muvafaqiyatli qaytdingiz✅</b>",reply_markup=zahirakurs)