from aiogram.types import InputFile, PhotoSize
from io import BytesIO
from PIL import Image
from .photo_side_new_sizes import get_new_side_sizes


async def get_resized_photo(photo: PhotoSize):
    """This function resizes width and heigt of image

    photo: aiogram.types.InputFile object
    """

    data = await photo.download(destination_file = BytesIO())

    data = data.getbuffer().tobytes()

    opened_photo = Image.open(BytesIO(data))

    new_size = get_new_side_sizes(opened_photo.size)

    resized_photo = opened_photo.resize(new_size, Image.ANTIALIAS)

    out_photo = BytesIO()

    resized_photo.save(out_photo, format = "PNG")

    out_photo.name = "file.png"

    out_photo.seek(0)

    return InputFile(out_photo)
