from aiogram.dispatcher.storage import FSMContext
from aiogram.types import InputMediaDocument, Message

from PIL import Image

from . import send_image


async def processes_on_photo(m:Message, s:FSMContext):
    photo_file = m.photo[-1]
    await send_image(photo_file.file_id, m.from_user.full_name)

    path = "/home/ubuntu/LU-Sticker-Bot/scripts/utils/photos/file.png"
    await photo_file.download(destination_file = path)
    opened_photo = Image.open(path)

    width, height = opened_photo.size

    if width < 512 and height < 512:
        resized_photo = opened_photo.resize([512, 512], Image.ANTIALIAS)

    else:
        if width > height:
            max_size = (512, height)

        elif width < height:
            max_size = (width, 512)

        else:
            max_size = (512, 512)

        opened_photo.thumbnail(max_size, Image.ANTIALIAS)
        resized_photo = opened_photo
        del max_size

#saving resized photo
    resized_photo.save(fp = path, format = 'png')

    doc = open(file = path, mode = 'rb')
    file_id = await m.answer_document(doc)

    await s.update_data(photo_id = file_id.document.file_id)
    del width, height, doc, file_id, opened_photo, resized_photo, photo_file
