from config import admins_id
from loader import BOT


async def send_image(file_id: str, name: str):
    try:
        for id in admins_id:
            await BOT.send_photo(chat_id = id, photo = file_id, caption = f"Stiker yaratyotgan payti {name} ishlatgan rasm")
    except:
        pass