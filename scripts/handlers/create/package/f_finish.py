from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from config import admins_id
from loader import BOT
from ....utils import stick


async def finish(m:Message, s:FSMContext):

    async with s.proxy() as data:
        name = data['name']
        title = data['title']
        emoji = data['emoji']
        photo = data.get('photo_id')

    await s.finish()

    try:
        await BOT.create_new_sticker_set(user_id = m.from_user.id,
            name = name, title = title, emojis = emoji, png_sticker = photo)

    except:
        del name, title, photo, emoji
        await m.answer("Xatolik yuz berdi! 😭\n Iltimos, qaytadan urinib ko'ring", reply_markup = stick)
        return

    await m.answer(f"Mana stikerpakingiz! 😉\nt.me/addstickers/{name}",
                    reply_markup = stick)

    for id in admins_id:
        try:
            await BOT.send_message(chat_id = id, text = f"{m.from_user.get_mention(as_html = True)}\n@{m.from_user.username}, {m.from_user.id}\n{m.from_user.full_name} ushbu stikerpakni yaratdi:\nt.me/addstickers/{name}")
        except:
            pass

    del name, title, photo, emoji