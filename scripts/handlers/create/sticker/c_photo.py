from aiogram.dispatcher.storage import FSMContext
from aiogram.types import ContentType, Message

from loader import DP
from ....utils import processes_on_photo


@DP.message_handler(state = 'ansts_photo', content_types = ContentType.PHOTO)
async def ansts_photo(msg: Message, state: FSMContext):
    await msg.answer_chat_action('upload_document')
    await processes_on_photo(msg, state)
    await msg.answer("Endi... Emoji yuboring!")
    await state.set_state('ansts_emoji')


@DP.message_handler(state = 'ansts_photo', content_types = ContentType.ANY)
async def ansts_photo_wrong(msg: Message):
    await msg.answer("Iltimos, bitta RASM yuboring!\n\nYoki to'xtating /cancel")