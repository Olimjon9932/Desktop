from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.inline_buttons import inline_tugmalar
#
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(text=f"Salom, {message.from_user.full_name}! Siz botdan foydalanishni boshladingiz\n",reply_markup=inline_tugmalar)

@dp.callback_query_handler(text = "2-amal")
async def orqaga(info: types.CallbackQuery):
    await info.message.answer(reply_markup=inline_tugmalar)

