from aiogram.types import InputFile, PhotoSize
from io import BytesIO
from PIL import Image
from .photo_side_new_sizes import get_new_side_sizes


async def get_resized_photo(photo: PhotoSize):
    """This function resizes width and heigt of image

    photo: aiogram.types.InputFile object
    """

    downloaded_photo: BytesIO = await photo.download(destination_file = BytesIO())

    downloaded_photo_bytes = downloaded_photo.getbuffer().tobytes()

    opened_photo: Image.Image = Image.open(BytesIO(downloaded_photo_bytes))

    new_size = get_new_side_sizes(opened_photo.size)

    resized_photo: Image.Image = opened_photo.resize(new_size, Image.ANTIALIAS)

    ready_photo = BytesIO()

    resized_photo.save(ready_photo, format = "PNG")

    ready_photo.name = "file.png"

    ready_photo.seek(0)

    return InputFile(ready_photo)
