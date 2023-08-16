from aiogram.dispatcher.filters import BoundFilter
from aiogram.types.message import Message

import re


class IsNameFilter(BoundFilter):
    def __init__(self) -> None:
        self.k_to_l = {'А':'A', 'Б':'B', 'В':'V', 'Г':'G', 'Д':'D', 'Е':'Ye', 'Ё':'Yo', 'Ж':'J', 'З':'Z', 'И':'I', 'Й':'Y', 'К':'K', 'Л':'L', 'М':'M', 'Н':'N', 'О':'O', 'П':'P', 'Р':'R', 'С':'S', 'Т':'T', 'У':'U', 'Ф':'F', 'Х':'X', 'Ч':'Ch', 'Ш':'Sh', 'Щ':'Sh', 'Ь':'', 'Ъ':'', 'Ы':'I', 'Э':'E', 'Ю':'Yu', 'Я':'Ya', }#and little
        super(IsNameFilter, self).__init__()

    async def check(self, msg:Message):
        result = re.findall(r'[a-zA-Z]+\d*', msg.text)
        if not result:
            return False

        name = msg.text.replace(' ', '_')
        return {'sticker_set_name': name}