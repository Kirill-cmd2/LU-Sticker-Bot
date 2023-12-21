from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message

from config import addition
from loader import BOT
from utils import stick, err_notify_admins


async def finish(m: Message, s: FSMContext):
    """
    Final function for adding sticker to stickerpack

    m: Message object
    s: Finite State Machine Context object
    """
    async with s.proxy() as data:
        name = data['name']
        emoji = data['emoji']
        photo = data['photo_id']

    await s.finish()

    # adding bot's username to stickerpack name
    name+=addition

    try:
        await BOT.add_sticker_to_set(user_id = m.from_user.id,
            name = name, emojis = emoji, png_sticker = photo)
    
    except:
        await m.answer("Xatolik yuz berdi!\nQaytadan urinib ko'ring:", reply_markup = stick)
        await err_notify_admins("Error occurred while adding sticker", m.from_user.id)
        return

    else:
        await m.answer(f"Stikeringizni qo'shdim!\nt.me/addstickers/{name}\n",
                    reply_markup = stick)
