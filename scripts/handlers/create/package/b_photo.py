from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType, Message

from loader import DP
from ....utils import processes_on_photo


@DP.message_handler(state = 'cnss_photo', content_types = ContentType.PHOTO)
async def cnss_photo(msg:Message, state:FSMContext):
    await msg.answer_chat_action('upload_document')
    await processes_on_photo(msg, state)
    await msg.answer("Endi esa... yuborgan rasmingizni ifodalovchi emoji yuboring.😀")
    await state.set_state('cnss_emoji')


@DP.message_handler(state = 'cnss_photo', content_types = ContentType.ANY)
async def wrong_photo(msg: Message):
    await msg.answer("Iltimos, bitta RASM yuboring!\n\nYoki to'xtating /cancel")