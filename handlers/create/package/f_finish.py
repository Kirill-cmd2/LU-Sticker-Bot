from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from config import addition
from loader import BOT
from utils import err_notify_admins, stick


async def finish(m: Message, s: FSMContext):
    """
    Final function for creating stickerpack

    m: Message object
    s: Finite State Machine Context object
    """
    async with s.proxy() as data:
        name = data['name']
        title = data['title']
        emoji = data['emoji']
        photo = data.get('photo_id')

    await s.finish()

    # adding bot's username to stickerpack name
    name+=addition

    try:
        await BOT.create_new_sticker_set(user_id = m.from_user.id,
            name = name, title = title, emojis = emoji, png_sticker = photo)

    except:
        await m.answer("Xatolik yuz berdi! 😭\n Iltimos, qaytadan urinib ko'ring", reply_markup = stick)
        await err_notify_admins("Some error occured in f_finish.py while creating a stickerpack", m.from_user.id)
        return
    
    else:
        await m.answer(f"Mana stikerpakingiz! 😉\nt.me/addstickers/{name}",
                    reply_markup = stick)
