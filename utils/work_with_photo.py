from aiogram.types import InputFile, PhotoSize
from io import BytesIO
from PIL import Image
from config import PHOTO_SIDE_MAX_SIZE


async def get_resized_photo(photo: PhotoSize):
    """This function resizes width and heigt of image

    photo: aiogram.types.InputFile object
    """

    #creating BytesOI object
    file_in_io = BytesIO()

    data = await photo.download(destination_file = file_in_io)

    data = data.getbuffer().tobytes()

    opened_photo = Image.open(BytesIO(data))

    width, height = opened_photo.size

    if width > height:
        new_width = PHOTO_SIDE_MAX_SIZE
        new_height = int((height / width) * PHOTO_SIDE_MAX_SIZE)
    elif height > width:
        new_height = PHOTO_SIDE_MAX_SIZE
        new_width = int((width / height) * PHOTO_SIDE_MAX_SIZE)

    resized_photo = opened_photo.resize((new_width, new_height), Image.ANTIALIAS)

    out_photo = BytesIO()

    resized_photo.save(out_photo, format = "PNG")

    out_photo.name = "file.png"

    out_photo.seek(0)

    return InputFile(out_photo)
