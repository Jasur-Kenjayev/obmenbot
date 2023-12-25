from loader import dp
from data.config import ADMINS
from keyboards.inline.Menuin import zkurs, kurszaxirr
from keyboards.default.menu import uzcard, Menu, bekor
from states.stett import PersonalData
from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.types import Message, CallbackQuery


@dp.message_handler(text="📊 Kurs | 💰Zahira")
async def kursvzax(message:
	Message):
	qiwif = open("kurs/qiwi.txt", "r")
	payerf = open("kurs/payeer.txt", "r")
	payerrubf = open("kurs/payeerrubl.txt", "r")
	
	qiwifo = open("kurs/qiwio.txt", "r")
	payerfo = open("kurs/payeero.txt", "r")
	payerrubfo = open("kurs/payeerrublo.txt", "r")
	await message.answer(f"<b>📈Sotish kursi</b>\n1 QIWI RUB = {qiwif.read()} UZS\n1 PAYEER RUB = {payerrubf.read()} UZS\n1 PAYEER USD = {payerf.read()} UZS\n\n<b>📈Olish kursi</b>\n1 QIWI RUB = {qiwifo.read()} UZS\n1 PAYEER RUB = {payerrubfo.read()} UZS\n1 PAYEER USD = {payerfo.read()} UZS",reply_markup=zkurs)

@dp.callback_query_handler(text_contains="zakurs")
async def zaxrt(call: CallbackQuery):
    uzcardz = open("zahira/uzcardz.txt", "r")
    qiwiz = open("zahira/qiwiz.txt", "r")
    payeerz = open("zahira/payeerz.txt", "r")
    usdz = open("zahira/payeerusd.txt", "r")
    await call.message.answer(f"<b>💰Obmennik Zahirasi</b>\n\n<i>UZCARD = {uzcardz.read()} UZS\nQIWI RUB = {qiwiz.read()} RUB\nPAYEER RUB = {payeerz.read()} RUB\nPAYEER USD = {usdz.read()} USD</i>",reply_markup=kurszaxirr)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="korishk")
async def koriw(call: CallbackQuery):
	qiwif = open("kurs/qiwi.txt", "r")
	payerf = open("kurs/payeer.txt", "r")
	payerrubf = open("kurs/payeerrubl.txt", "r")
	qiwifo = open("kurs/qiwio.txt", "r")
	payerfo = open("kurs/payeero.txt", "r")
	payerrubfo = open("kurs/payeerrublo.txt", "r")
	await call.message.answer(f"<b>📈Sotish kursi</b>\n1 QIWI RUB = {qiwif.read()} UZS\n1 PAYEER RUB = {payerrubf.read()} UZS\n1 PAYEER USD = {payerf.read()} UZS\n\n<b>📈Olish kursi</b>\n1 QIWI RUB = {qiwifo.read()} UZS\n1 PAYEER RUB = {payerrubfo.read()} UZS\n1 PAYEER USD = {payerfo.read()} UZS",reply_markup=zkurs)
	await call.message.delete()
	await call.answer(cache_time=60)