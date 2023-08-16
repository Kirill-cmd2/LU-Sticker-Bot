from aiogram.dispatcher.storage import FSMContext
from aiogram.types import ContentType, Message

from filters import IsNameFilter
from loader import DP
from utils import cnssStates

from .f_finish import finish


@DP.message_handler(IsNameFilter(), state = cnssStates.cnss_name)
async def cnss_name(msg: Message, state: FSMContext, sticker_set_name):
    await msg.answer_chat_action('typing')
    await state.update_data(name = sticker_set_name)

    await finish(m = msg, s = state)


@DP.message_handler(state = cnssStates.cnss_name)
async def wrong_name(msg: Message):
    await msg.answer("Faqat lotin harflari va raqamlar ishlatilishi mumkin!\n\nQaytadan yozing!")


@DP.message_handler(state = cnssStates.cnss_name, content_types=ContentType.ANY)
async def wrong_name_any(msg: Message):
    await msg.answer("Iltimos, nomni kiriting")
