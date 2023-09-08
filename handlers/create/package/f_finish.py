from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from config import addition
from loader import BOT
from utils import stick


async def finish(m:Message, s:FSMContext):

    async with s.proxy() as data:
        name = data['name']
        title = data['title']
        emoji = data['emoji']
        photo = data.get('photo_id')

    await s.finish()

    name+=addition
    try:
        await BOT.create_new_sticker_set(user_id = m.from_user.id,
            name = name, title = title, emojis = emoji, png_sticker = photo)

    except:
        await m.answer("Xatolik yuz berdi! 😭\n Iltimos, qaytadan urinib ko'ring", reply_markup = stick)
        return

    await m.answer(f"Mana stikerpakingiz! 😉\nt.me/addstickers/{name}",
                    reply_markup = stick)
