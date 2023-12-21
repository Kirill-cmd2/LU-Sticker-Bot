import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode

from config import TOKEN
# from database import StickBotDatabase


BOT = Bot(TOKEN, parse_mode = ParseMode.HTML)
DP = Dispatcher(BOT, storage = MemoryStorage())
# DB = StickBotDatabase(loop=DP.loop)


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s', level=logging.INFO)

__all__ = ['BOT', 'DP']#, 'DB']
