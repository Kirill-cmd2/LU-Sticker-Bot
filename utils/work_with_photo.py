from aiogram.dispatcher.storage import FSMContext
from aiogram.types import InputFile, Message
from io import BytesIO
from PIL import Image

from config import admins_id
from loader import DP
# can send photo not document and in finish function use png_sticker

async def processes_on_photo(m:Message, s:FSMContext):
    """This function resizes width and heigt of image

    m: aiogram.types.Message
    s: aiogram.dispatcher.storage.FSMContext
    """
    # source_message = m.reply_to_message
    # photo = source_message.photo[-1]
    # photo = await photo.download(destination = BytesIO())
    # --resize photo--
    # input_file = InputFile(path_or_bytesio = photo)


    photo_file = m.photo[-1]

    # await photo_file.download() - file will be downloaded to LU Stick Bot/
    path = "/home/bubish/Desktop/Programming/Python/bots/LU Stick Bot/utils/photos/file.png"

    try:
        await photo_file.download(destination_file = path)
    except:
        try:
            for id in admins_id:
                await DP.bot.send_message(chat_id = id, text = "Some error occured in working_with_photo while downloading photo")
        except:
            pass

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

    doc = InputFile(path_or_bytesio = path)
    file_id = await m.answer_document(doc)

    await s.update_data(photo_id = file_id.document.file_id)
    del width, height, doc, file_id, opened_photo, resized_photo, photo_file
