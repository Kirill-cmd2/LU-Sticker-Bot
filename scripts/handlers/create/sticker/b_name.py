from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message

from ....filters import IsNameFilter
from loader import DP


@DP.message_handler(IsNameFilter(), state = 'ansts_name')
async def cnss_name(msg: Message, state: FSMContext, sticker_set_name):
    await state.update_data(name = sticker_set_name)
    await msg.answer("Rasm kerak...")
    await state.set_state('ansts_photo')