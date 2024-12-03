from aiogram.dispatcher.storage import FSMContext
from aiogram.types import ContentType, Message

from filters import IsNameFilter
from loader import DP
from utils import anstsStates


@DP.message_handler(IsNameFilter(), state = anstsStates.ansts_name)
async def cnss_name(msg: Message, state: FSMContext, sticker_set_name):
    await state.update_data(name = sticker_set_name)
    await msg.answer("Rasm kerak...")

    await anstsStates.ansts_photo.set()


@DP.message_handler(state = anstsStates.ansts_name, content_types=ContentType.ANY)
async def wrong_name(msg: Message):
    await msg.answer("Iltimos, stikerpak nomini kiriting")