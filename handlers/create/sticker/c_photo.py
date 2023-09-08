from aiogram.dispatcher.storage import FSMContext
from aiogram.types import ContentType, Message

from loader import DP
from utils import anstsStates, processes_on_photo


@DP.message_handler(state = anstsStates.ansts_photo, content_types = ContentType.PHOTO)
async def ansts_photo(msg: Message, state: FSMContext):
    await msg.answer_chat_action('upload_document')

    doc_id = await processes_on_photo(msg)
    await state.update_data(photo_id = doc_id)

    await msg.answer("Endi... Emoji(lar) yuboring!")

    await anstsStates.ansts_emoji.set()


@DP.message_handler(state = anstsStates.ansts_photo, content_types = ContentType.ANY)
async def ansts_photo_wrong(msg: Message):
    await msg.answer("Iltimos, bitta RASM yuboring!\n\nYoki to'xtating /cancel")