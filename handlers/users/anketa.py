from aiogram import types
from aiogram.dispatcher import FSMContext

from states.holatlar import Holat
from loader import dp

infos = {}
# Echo bot
@dp.message_handler(text = "anketa toldirish")
async def bot_echo(message: types.Message):
    await message.answer(text="Ismingizni kiriting: ")
    await Holat.Ism.set()

@dp.message_handler(state=Holat.Ism)
async def bot_echo(message: types.Message):
    ism = message.text
    infos['ism'] = ism
    await message.answer(text="Familyangizni kiriting: ")
    await Holat.Fam.set()

@dp.message_handler(state=Holat.Fam)
async def bot_echo(message: types.Message, state: FSMContext):
    fam = message.text
    infos['fam'] = fam
    await message.answer(text='Yoshni kiriting')
    await Holat.Yosh.set()

