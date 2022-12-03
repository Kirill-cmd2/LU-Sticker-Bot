from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import CancelHandler
from aiogram.types.message import Message


class IsNameFilter(BoundFilter):
    def __init__(self) -> None:
        self.all_eng_let = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
        self.all_eng_let_and_nums = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '_'}

    async def check(self, msg:Message):
        j = msg.text[0]
        if j in self.all_eng_let:
            pass
        else:
            await msg.answer("Stikerpak ssilkasi uchun kiritiladigan nom LOTIN HARFI bilan boshlanishi kerak!")
            raise CancelHandler()

        for letter in msg.text:
            if letter in self.all_eng_let_and_nums:
                pass
            else:
                # replace Kirillic to Latin
                await msg.answer("LOTIN HARFLARI va RAQAMLAR ishlatilishi mumkin, xolos!\nIltimos, to'g'irlab yozing...\n\nYoki to'xtating /cancel")
                raise CancelHandler()

        name = msg.text.replace(' ', '_') + "_by_lu_sticker_bot"
        return {'sticker_set_name': name}
