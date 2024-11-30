from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType, Message

from loader import DP
from utils import cnssStates, get_resized_photo


@DP.message_handler(state = cnssStates.cnss_photo, content_types = ContentType.PHOTO)
async def cnss_photo(msg:Message, state:FSMContext):
    await msg.answer_chat_action('upload_document')

    file_to_send = await get_resized_photo(msg.photo[-1])

    sent_file = await msg.answer_document(file_to_send)

    await state.update_data(photo_id = sent_file.document.file_id)

    await msg.answer("Endi esa... yuborgan rasmingizni ifodalovchi emoji(lar) yuboring.😀")

    await cnssStates.cnss_emoji.set()


@DP.message_handler(state = cnssStates.cnss_photo, content_types = ContentType.ANY)
async def wrong_photo(msg: Message):
    # await msg.delete()
    await msg.answer("Iltimos, bitta RASM yuboring!\n\nYoki to'xtating /cancel")