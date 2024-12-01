from aiogram.types import PhotoSize
from PIL import Image
from .download_photo import download_photo
from .resize_photo import resize_photo
from .prepare_photo import get_ready_photo


async def get_resized_photo(photo: PhotoSize):
    """This function resizes width and heigt of image

    photo: aiogram.types.InputFile object
    """

    downloaded_photo = await download_photo(photo)

    opened_photo: Image.Image = Image.open(downloaded_photo)

    resized_photo = resize_photo(opened_photo)

    ready_photo = get_ready_photo(resized_photo,
                                    photo_name = "file.png",
                                    photo_format = "PNG")

    return ready_photo
