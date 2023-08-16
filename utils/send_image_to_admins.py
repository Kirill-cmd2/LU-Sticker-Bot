from config import admins_id
from loader import BOT


async def send_image(file_id: str, name):
    try:
        for id in admins_id:
            await BOT.send_photo(chat_id = id, photo = file_id, caption = f"Stiker yaratyotgan payti {name.from_user.get_mention(as_html=True)} ishlatgan rasm")
    except:
        pass