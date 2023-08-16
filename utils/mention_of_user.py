from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import admins_id


async def creating_mention(msg, text_to_user):
    user_id=msg.from_user.id
    url=f'tg://user?id={user_id}'

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton('User', url)]])

    await msg.bot.send_message(chat_id=admins_id[0], text=text_to_user, reply_markup=keyboard)
