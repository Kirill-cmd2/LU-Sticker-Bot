from aiogram.types import Message, InputFile, ContentType
from aiogram.dispatcher.storage import FSMContext
from loader import DP

from io import BytesIO
from PIL import Image

async def processes_on_photo(m:Message, s:FSMContext):
    photo_file_id = m.photo[-1]
    photo_in_bytes = await photo_file_id.download(destination_file = BytesIO())
    
    image.seek(0)
    img = Image.open(image)
    image = img.resize((512, 512), Image.ANTIALIAS)
    image.save(BytesIO(), format="png")#, optimize=True, quality=Quality)

    input_file = InputFile(path_or_bytesio = photo_in_bytes)
    file_id = await m.answer_document(input_file)

@DP.message_handler(content_types=ContentType.PHOTO)
async def something(msg:Message, state:FSMContext):
    await processes_on_photo(msg, state)


if __name__ == '__main__':
    from aiogram.utils.executor import start_polling
    start_polling(dispatcher = DP,
                skip_updates = True)
