from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

tugmalar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Qo'shish"),
            KeyboardButton(text="Ayirish"),
            KeyboardButton(text="Ko'paytirish"),
            KeyboardButton(text="Bo'lish"),
            KeyboardButton(text="anketa toldirish")

        ],

    ],
  resize_keyboard=True
)