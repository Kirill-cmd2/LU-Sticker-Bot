from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import CancelHandler
from aiogram.types.message import Message

from .UNICODE_EMOJI_ENGLISH import UNICODE_EMOJI_ENGLISH


class IsEmojiFilter(BoundFilter):
    async def check(self, msg: Message):
        if msg.text in UNICODE_EMOJI_ENGLISH:
            return True
        else:
            await msg.answer("Iltimos, BITTA EMOJI yuboring!\n\nYoki to'xtating /cancel")
            raise CancelHandler()