from aiogram.dispatcher.storage import FSMContext
from aiogram.types import ContentType, Message

from loader import DP
from utils import anstsStates, get_resized_photo


@DP.message_handler(state = anstsStates.ansts_photo, content_types = ContentType.PHOTO)
async def ansts_photo(msg: Message, state: FSMContext):
    await msg.answer_chat_action('upload_document')

    file_to_send = await get_resized_photo(msg.photo[-1])

    sent_file = await msg.answer_document(file_to_send)

    await state.update_data(photo_id = sent_file.document.file_id)

    await msg.answer("Endi... Emoji(lar) yuboring!")

    await anstsStates.ansts_emoji.set()


@DP.message_handler(state = anstsStates.ansts_photo, content_types = ContentType.ANY)
async def ansts_photo_wrong(msg: Message):
    await msg.answer("Iltimos, bitta RASM yuboring!\n\nYoki to'xtating /cancel")