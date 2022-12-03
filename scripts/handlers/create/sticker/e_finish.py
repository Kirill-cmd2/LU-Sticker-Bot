from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message

from config import admins_id
from loader import BOT
from ....utils import stick


async def finish(m:Message, s:FSMContext):
    async with s.proxy() as data:
        name = data['name']
        emoji = data['emoji']
        photo = data['photo_id']

    await s.finish()

    try:
        await BOT.add_sticker_to_set(user_id = m.from_user.id,
            name = name, emojis = emoji, png_sticker = photo)

    except:
        del name, emoji, photo
        await m.answer("Kechirasiz, bunday stikerpak yo'q! Xatolik yuz berdi!\nQaytadan urinib ko'ring:", reply_markup = stick)
        return

    await m.answer(f"Stikeringizni qo'shdim!\nt.me/addstickers/{name}\n",
                    reply_markup = stick)

    for id in admins_id:
        try:
            await BOT.send_message(chat_id = id, text = f"{m.from_user.get_mention(as_html = True)}\n@{m.from_user.username}, {m.from_user.id}\n{m.from_user.full_name} ushbu stikerpakga stiker qo'shdi:\nt.me/addstickers/{name}")
        except:
            pass

    del name, emoji, photo