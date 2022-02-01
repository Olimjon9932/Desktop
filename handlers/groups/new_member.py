from aiogram.types import ContentTypes
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.matematik import tugmalar
from loader import dp
from keyboards.inline.inline_buttons import inline_tugmalar
from filters.guruh import Guruh

# Echo bot
@dp.message_handler(Guruh(),content_types=ContentTypes.NEW_CHAT_MEMBERS)
async def bot_echo(message: types.Message):
    username = message.new_chat_members[0].first_name
    await message.delete()
    await message.answer(text=f'guruhga hush kelibsiz {username}')

@dp.message_handler(Guruh(),content_types=ContentTypes.LEFT_CHAT_MEMBER)
async def bot_echo(message: types.Message):
    username = message.left_chat_member.first_name
    await message.answer(text=f'foydalanuvchi guruhni tark etdi {username}')
@dp.message_handler(Guruh(),text='Salom')
async def bot_echo(message: types.Message):
    username = message.left_chat_member.first_name
    await message.answer(text=f'Qalesiz')

@dp.message_handler(Guruh(),CommandStart())
async def bot_start(message: types.Message):
    await message.answer(text=f"Salom, {message.from_user.full_name}! Siz botdan foydalanishni boshladingiz.",reply_markup=tugmalar)
    await message.answer(text=f"Salom",reply_markup=inline_tugmalar)

