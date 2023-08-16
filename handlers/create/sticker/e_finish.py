from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message
from aiogram.utils.exceptions import InvalidStickersSet

from config import admins_id, addition
from loader import BOT
from utils import stick


async def finish(m:Message, s:FSMContext):
    async with s.proxy() as data:
        name = data['name']
        emoji = data['emoji']
        photo = data['photo_id']

    await s.finish()

    try:
        await BOT.add_sticker_to_set(user_id = m.from_user.id,
            name = name+addition, emojis = emoji, png_sticker = photo)

    except InvalidStickersSet:
        del name, emoji, photo
        await m.answer("Xatolik yuz berdi!\nKechirasiz, bunday stikerpak yo'q!\nQaytadan urinib ko'ring:", reply_markup = stick)
        return
    except:
        del name, emoji, photo
        await m.answer("Xatolik yuz berdi!\nQaytadan urinib ko'ring:", reply_markup = stick)
        return

    await m.answer(f"Stikeringizni qo'shdim!\nt.me/addstickers/{name}\n",
                    reply_markup = stick)

    for id in admins_id:
        try:
            await BOT.send_message(chat_id = id, text = f"{m.from_user.get_mention(as_html = True)}\n{m.from_user.id}\nAdd sticker to this stickerpack:\nt.me/addstickers/{name+addition}")
        except:
            pass

    del name, emoji, photo