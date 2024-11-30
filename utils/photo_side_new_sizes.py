from config import PHOTO_SIDE_MAX_SIZE


def get_new_side_sizes(size: tuple[int, int]):
    width, height = size

    if width > height:
        new_width = PHOTO_SIDE_MAX_SIZE
        new_height = int((height / width) * PHOTO_SIDE_MAX_SIZE)
    elif height > width:
        new_height = PHOTO_SIDE_MAX_SIZE
        new_width = int((width / height) * PHOTO_SIDE_MAX_SIZE)
    
    return (new_width, new_height)
