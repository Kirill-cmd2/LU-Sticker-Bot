from aiogram.types import InputFile
from io import BytesIO
from PIL import Image


def get_ready_photo(resized_photo: Image.Image, *, photo_name: str, photo_format):
    ready_photo = BytesIO()

    resized_photo.save(ready_photo, format = photo_format)

    ready_photo.name = photo_name

    ready_photo.seek(0)

    return InputFile(ready_photo)
