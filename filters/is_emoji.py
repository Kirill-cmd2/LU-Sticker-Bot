from aiogram.dispatcher.filters import BoundFilter
from aiogram.types.message import Message

from .UNICODE_EMOJI_ENGLISH import UNICODE_EMOJI_ENGLISH


class IsEmojiFilter(BoundFilter):
    def __init__(self):
        self.list_of_emojis = []
        super().__init__()

    async def check(self, msg: Message):
        for an_emoji in msg.text:
            if an_emoji in UNICODE_EMOJI_ENGLISH:
                self.list_of_emojis.append(an_emoji)

        if not self.list_of_emojis:
            return False

        return {'emoji_list': self.list_of_emojis}
