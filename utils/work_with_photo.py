from aiogram.types import InputFile, PhotoSize
from io import BytesIO
from PIL import Image


async def get_resized_photo(photo: PhotoSize):
    """This function resizes width and heigt of image

    msg: aiogram.types.Message object
    """

    #creating BytesOI object
    file_in_io = BytesIO()

    # initializing file and downloading photo
    data = await photo.download(destination_file = file_in_io)

    # converting _io.BytesIO to bytes-like object
    data = data.getbuffer().tobytes()

    opened_photo = Image.open(BytesIO(data))
    width, height = opened_photo.size

    if width < 512 and height < 512:
        opened_photo.resize([512, 512], Image.ANTIALIAS)

    else:
        if width > height:
            max_size = (512, height)

        elif width < height:
            max_size = (width, 512)
        else:
            max_size = (512, 512)

        opened_photo.thumbnail(max_size, Image.ANTIALIAS)

    #saving resized photo and giving name
    opened_photo.save(fp = file_in_io, format = 'PNG')
    file_in_io.name = "file.png"

    # seek() function goes to given byte
    file_in_io.seek(0)

    return InputFile(file_in_io)
