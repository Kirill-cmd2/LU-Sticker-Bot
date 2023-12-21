from aiogram.dispatcher.storage import FSMContext
from aiogram.types import ContentType, Message

from loader import DP
from utils import delstickerStates, stick


@DP.message_handler(state = delstickerStates.delstick, content_types = ContentType.STICKER)
async def del_stick(msg:Message, state:FSMContext):
    await state.finish()

    try:
        await msg.sticker.delete_from_set()

    except:
        await msg.answer("Xatolik yuz berdi!\nUshbu stiker sizga tegishli emas! Iltimos, qaytadan boshlab o'zingiznikini yuboring",
            reply_markup = stick)
    
    else:
        await msg.reply("O'chirib, yo'q qilib yubordim!")