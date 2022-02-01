from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .azo_bolish import Asosiy_checking


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(Asosiy_checking())
