import logging
from aiogram.types import Message, CallbackQuery
from loader import dp
from keyboards.inline.Menuin import categoryMenu, ortga
from keyboards.default.menu import uzcard, Menu, bekor
from states.stett import PersonalData
from aiogram.dispatcher import FSMContext
from aiogram import types

@dp.message_handler(text= "◀️ Orqaga",state=PersonalData)
async def cance(message:
	types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>🤖Orqaga Muvafaqiyatli qaytdingiz✅</b>",reply_markup=uzcard)
	
@dp.message_handler(text= "🔚 Bosh Menu")
async def nazat(message:
	Message):
	await message.answer("<b>🤖Orqaga Muvafaqiyatli qaytdingiz✅</b>",reply_markup=Menu)
	
@dp.message_handler(text="💳 Hamyonlar")
async def wallet(message:
	Message):
	await message.answer("<b>🗂 Marhamat hamyoningizni kiriting👇</b>",reply_markup=uzcard)
		
@dp.message_handler(text="➕ UZCARD")
async def create_wal(message: Message):
    try:
    	id = message.from_user.id
    	follow = open(f"files/uzcard{id}.txt", "r")
    	await message.answer(f"<b>💎 Sizning UZCARD Raqamingiz👇\n\n📌 UZCARD - <i>{follow.read()}</i>\n\n💳 UZCARD raqamni o'zgartirishni xoxlasangiz shu yerga yangi UZCARD raqam kiriting👇</b>",reply_markup=bekor)
    except:
    	await message.answer("<b>🔖 UZCARD raqamingizni kiriting Bo'sh joylar yoki boshqa belgilarsiz.\n\n✅ Namuna: 9860080181620333</b>",reply_markup=bekor)
    await PersonalData.aduzcard.set()
    
@dp.message_handler(state=PersonalData.aduzcard)
async def wallet(message:
	Message, state: FSMContext):
	id = message.from_user.id
	follw = message.text
	msgw = follw
	if len(follw) != 16 or (not follw.isdigit()):
		await message.answer("<b>💳 UZCARD raqam formati notog'ri namunada ko'rsatilgandek kiriting👇\n\n✅ Namuna👉 9860080181620333</b>")
	else:
			follow = open(f"files/uzcard{id}.txt", "w")
			follow.write(follw)
			follow.close()
			await state.finish()
			await message.answer("<b>UZCARD raqamingiz kiritildi ✅</b>",reply_markup=uzcard)

@dp.message_handler(text="➕ PAYEER")
async def create_pay(message: Message):
    try:
    	id = message.from_user.id
    	payeer = open(f"files/payeer{id}.txt", "r")
    	await message.answer(f"<b>💎 Sizning PAYEER Raqamingiz👇\n\n📌 PAYEER - <i>{payeer.read()}</i>\n\n💳 PAYEER raqamni o'zgartirishni xoxlasangiz shu yerga yangi PAYEER raqam kiriting👇</b>",reply_markup=bekor)
    except:
    	await message.answer("<b>🔖 PAYEER raqamingizni kiriting Bo'sh joylar yoki boshqa belgilarsiz.\n\n✅ Namuna: P1068613774</b>",reply_markup=bekor)
    await PersonalData.adpayeer.set()
    
@dp.message_handler(state=PersonalData.adpayeer)
async def wallet_payeer(message:
	Message, state: FSMContext):
	id = message.from_user.id
	payeerm = message.text
	if len(payeerm) != 11:
		await message.answer("<b>💳 PAYEER raqam formati notog'ri namunada ko'rsatilgandek kiriting👇\n\n✅ Namuna👉 P1068613774</b>")
	else:
			payeer = open(f"files/payeer{id}.txt", "w")
			payeer.write(payeerm)
			payeer.close()
			await state.finish()
			await message.answer("<b>PAYEER raqamingiz kiritildi ✅</b>",reply_markup=uzcard)

@dp.message_handler(text="➕ QIWI")
async def create_qiwi(message: Message):
    try:
    	id = message.from_user.id
    	qiwi = open(f"files/qiwi{id}.txt", "r")
    	await message.answer(f"<b>💎 Sizning QIWI Raqamingiz👇\n\n📌 QIWI - <i>{qiwi.read()}</i>\n\n💳 QIWI raqamni o'zgartirishni xoxlasangiz shu yerga yangi QIWI raqam kiriting👇</b>",reply_markup=bekor)
    except:
    	await message.answer("<b>🔖 QIWI raqamingizni kiriting Bo'sh joylar yoki boshqa belgilarsiz.\n\n✅ Namuna: <i>+998945142452</i></b>",reply_markup=bekor)
    await PersonalData.adqiwi.set()
    
@dp.message_handler(state=PersonalData.adqiwi)
async def wallet_qiwi(message:
	Message, state: FSMContext):
	id = message.from_user.id
	qiwim = message.text
	if len(qiwim) != 13:
		await message.answer("<b>💳 QIWI raqam formati notog'ri namunada ko'rsatilgandek kiriting👇\n\n✅ Namuna👉 +998945942452</b>")
	else:
		qiwi = open(f"files/qiwi{id}.txt", "w")
		qiwi.write(qiwim)
		qiwi.close()
		await state.finish()
		await message.answer("<b>QIWI raqamingiz kiritildi ✅</b>",reply_markup=uzcard)
