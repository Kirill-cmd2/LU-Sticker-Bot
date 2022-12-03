from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message

from ....filters import IsNameFilter
from loader import DP

from .f_finish import finish


@DP.message_handler(IsNameFilter(), state = 'cnss_name')
async def cnss_name(msg: Message, state: FSMContext, sticker_set_name):
    await msg.answer_chat_action('typing')
    await state.update_data(name = sticker_set_name)
    await finish(m = msg, s = state)