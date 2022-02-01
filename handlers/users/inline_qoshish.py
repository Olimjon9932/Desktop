from aiogram import types
from aiogram.types import CallbackQuery
from loader import dp


# Echo bot
@dp.message_handler(text='1-amal')
async def javob(malumot:CallbackQuery):
    await malumot.message.answer(text="Inline buttonsdan xabar yuborildi")
