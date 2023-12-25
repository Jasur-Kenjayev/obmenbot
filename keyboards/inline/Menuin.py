from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
    InlineKeyboardButton(text="UZCARD ♻️ QIWI RUB", callback_data="uzrub"),
    ],
    [
        InlineKeyboardButton(text="QIWI RUB ♻️ UZCARD", callback_data="rubuzs"),
    ],
    [
    InlineKeyboardButton(text="UZCARD ♻️ PAYEER RUB", callback_data="payuzsu"),
     ],
     [ InlineKeyboardButton(text="PAYEER RUB ♻️ UZCARD", callback_data="uzsbpayer"),
     ],
     [
     	InlineKeyboardButton(text="UZCARD ♻️ PAYEER USD", callback_data="PayerUsD"),
     ],
     [ 
        InlineKeyboardButton(text="PAYEER USD ♻️ UZCARD", callback_data="PusDuz"),
    ],
    [
    	InlineKeyboardButton(text="❌ Bekor qilish", callback_data="menbe"),
    ],
])

ortga = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="⬆️ Berishni kiritish * UZCARD", callback_data="uzcardo"),
    ],
    [
    	InlineKeyboardButton(text="❌ Bekor qilish", callback_data="menbe"),
    ],
])

qiwiuzcardo = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="⬆️ Berishni kiritish * QIWI RUB", callback_data="rublqwi"),
    ],
    [
    	InlineKeyboardButton(text="❌ Bekor qilish", callback_data="menbe"),
    ],
])

uzcardpayeerb = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="⬆️ Berishni kiritish * UZCARD", callback_data="uzbekpayer"),
    ],
    [
    	InlineKeyboardButton(text="❌ Bekor qilish", callback_data="menbe"),
    ],
])

payeeruzsr = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="⬆️ Berishni kiritish * PAYEER RUB", callback_data="rublpayeer"),
    ],
    [
    	InlineKeyboardButton(text="❌ Bekor qilish", callback_data="menbe"),
    ],
])

uzcardpayeerusd = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="⬆️ Berishni kiritish * UZCARD", callback_data="Dastusdp"),
    ],
    [
    	InlineKeyboardButton(text="❌ Bekor qilish", callback_data="menbe"),
    ],
])


payusduzcard = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="⬆️ Berishni kiritish * PAYEER USD", callback_data="payUsdi"),
    ],
    [
    	InlineKeyboardButton(text="❌ Bekor qilish", callback_data="menbe"),
    ],
])


zkurs = InlineKeyboardMarkup(
    inline_keyboard=[
    [
    	InlineKeyboardButton(text="📇 Zahirani Ko'rish", callback_data="zakurs"),
    ],
])

kurszaxirr = InlineKeyboardMarkup(
    inline_keyboard=[
    [
    	InlineKeyboardButton(text="💸 Kursni Ko'rish", callback_data="korishk"),
    ],
])