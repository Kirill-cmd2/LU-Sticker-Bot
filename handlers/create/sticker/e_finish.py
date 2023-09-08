from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message
from aiogram.utils.exceptions import InvalidStickersSet

from config import addition
from loader import BOT
from utils import stick


async def finish(m:Message, s:FSMContext):
    async with s.proxy() as data:
        name = data['name']
        emoji = data['emoji']
        photo = data['photo_id']

    await s.finish()

    name+=addition
    try:
        await BOT.add_sticker_to_set(user_id = m.from_user.id,
            name = name, emojis = emoji, png_sticker = photo)

    except InvalidStickersSet:
        await m.answer("Xatolik yuz berdi!\nKechirasiz, bunday stikerpak yo'q!\nQaytadan urinib ko'ring:", reply_markup = stick)
        return
    except:
        await m.answer("Xatolik yuz berdi!\nQaytadan urinib ko'ring:", reply_markup = stick)
        return

    await m.answer(f"Stikeringizni qo'shdim!\nt.me/addstickers/{name}\n",
                    reply_markup = stick)
