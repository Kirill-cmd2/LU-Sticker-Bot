from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import admins_id
from loader import BOT


async def err_notify_admins(text_to_user: str, chat_id=None):
    """
    Notifying admins about errors
    Also using inline keyboard to mention user

    text_to_user: Text which should be send to admin
    """
    url=f'tg://user?id={chat_id}'

    mention_of_user = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton('User', url)]])

    for id in admins_id:
        try:
            await BOT.send_message(chat_id = id,
                                      text = text_to_user,
                                      reply_markup = mention_of_user)
        except:
            continue
