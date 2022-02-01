from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from data.config import kanallar
from utils.azolikni_tekshirish import tekshirish
from loader import bot

class Asosiy_checking(BaseMiddleware):
    async def on_pre_proces_update(self,xabar:types.Update,data:dict):
        if xabar.message:
            user_id = xabar.message.from_user.id
        elif xabar.callback_query:
            user_id = xabar.callback_query.from_user.id
        else:
            return
        matn = 'Quyidagi kanalga azo boling\n'

        dastlabki_holati = True
        for k in kanallar:
            holat = await tekshirish(user_id=user_id,kanal=k)
            dastlabki_holati*=holat
            kanal = await bot.get_chat(k)
            if not holat:
                link = await kanal.export_invite_link()
                matn+=(f"👉 <a href='{link}'>{kanal.title}</a>\n")
        if not dastlabki_holati:
                await xabar.message.answer(matn,disable_web_page_preview=True,)
                raise CancelHandler()