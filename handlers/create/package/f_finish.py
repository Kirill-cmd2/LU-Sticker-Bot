from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from config import addition
from loader import DB, BOT
from utils import stick, creating_mention


async def finish(m:Message, s:FSMContext):
    async with s.proxy() as data:
        name = data['name']
        title = data['title']
        emoji = data['emoji']
        photo = data.get('photo_id')

    await s.finish()

    try:
        await BOT.create_new_sticker_set(user_id = m.from_user.id,
            name = name+addition, title = title, emojis = emoji, png_sticker = photo)

    except:
        del name, title, photo, emoji
        await m.answer("Xatolik yuz berdi! :loudly_crying_face:\n Iltimos, qaytadan urinib ko'ring", reply_markup = stick)
        return

    await m.answer(f"Mana stikerpakingiz! :winking_face:\nt.me/addstickers/{name+addition}",
                    reply_markup = stick)


    creating_mention(msg=m, text_to_user=f"{m.from_user.id}\nCreated this stickerpack:\nt.me/addstickers/{name+addition}")


    # DB.add_stickerpack_name(name = name, id = m.from_user.id)

    del name, title, photo, emoji