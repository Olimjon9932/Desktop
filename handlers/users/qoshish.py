from aiogram import types
from random import randint
from keyboards.inline.Orqaga import inline_tugmalar
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from loader import dp

natijalar =[]
javoblar= []
@dp.message_handler(text="Qo'shish")
async def bot_echo(message: types.Message):
    son1 = randint(1,100)
    son2 = randint(1,100)
    natija=son1+son2
    natijalar.append(natija)
    await message.answer(text=f'{son1}+{son2}=', reply_markup=inline_tugmalar)

