from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔄 Almashtirish"),
        ],
       [
       	KeyboardButton(text="💳 Hamyonlar"),
       	KeyboardButton(text="📊 Kurs | 💰Zahira"),
       ],
      [
      	KeyboardButton(text="♻️ Almashuvlar"),
       ],
       [
       	KeyboardButton(text="📞 Aloqa"),
      	KeyboardButton(text="🗞 Biz haqimizda"),
      ],
      [
      	KeyboardButton(text="🕘 Ish vaqti"),
       ],
    ],
    resize_keyboard=True,
)

bekor = ReplyKeyboardMarkup(
    keyboard = [
        [
        	KeyboardButton(text="◀️ Orqaga"),
        ],
     ],
     resize_keyboard=True
)
bekor2 = ReplyKeyboardMarkup(
    keyboard = [
        [
        	KeyboardButton(text="Orqaga ▶️"),
        ],
     ],
     resize_keyboard=True
)

uzcard = ReplyKeyboardMarkup(
    keyboard = [
        [
        	KeyboardButton(text="➕ UZCARD"),
        ],
        [
        KeyboardButton(text="➕ QIWI"),
        KeyboardButton(text="➕ PAYEER"),
        ],
        [
        KeyboardButton(text="🔚 Bosh Menu"),
     ],
  ],
     resize_keyboard=True
)