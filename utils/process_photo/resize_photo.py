from PIL import Image
from .photo_side_new_sizes import get_new_side_sizes


def resize_photo(photo: Image.Image):
    new_size = get_new_side_sizes(photo.size)

    resized_photo: Image.Image = photo.resize(new_size, Image.ANTIALIAS)

    return resized_photo
