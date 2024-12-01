from aiogram.types import PhotoSize
from io import BytesIO


async def download_photo(photo: PhotoSize):
    downloaded_photo: BytesIO = await photo.download(destination_file = BytesIO())

    downloaded_photo_bytes = downloaded_photo.getbuffer().tobytes()

    return BytesIO(downloaded_photo_bytes)
