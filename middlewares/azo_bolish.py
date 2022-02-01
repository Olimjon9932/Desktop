from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from data.config import kanallar
from utils import azolikni_tekshirish
from loader import bot

class Asosiy_checking(BaseMiddleware):
    async def asosiy(self, info:types.Update):
        if info.message:
            user_id = info.message.from_user.id
        elif info.callback_query:
            user_id = info.callback_query.from_user.id
        else:
            return
        matn = "Quyidagi kanallarga azo bo'ling\n"
        dastlabki_xolat = True
        for k in kanallar:
            holat = await azolikni_tekshirish.tekshir(user_id = user_id, kanal_link = k)
            dastlabki_xolat *= holat

            kanal = await bot.get_chat(k)
            if not holat:
                link = kanal.export_invite_link()
                matn += (f"<a href = '{link}'>{kanal.title}</a>\n")
            if not dastlabki_xolat:
                await info.message.answer(matn, disable_web_page_preview = True)
                raise CancelHandler()
