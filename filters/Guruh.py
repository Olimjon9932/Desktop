from aiogram.types import ChatType, Message
from aiogram.dispatcher.filters import BoundFilter

class Guruh(BoundFilter):
    async def check(self, info: Message):
        return info.chat.type == ChatType.SUPERGROUP