from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import Message

from config import admins_id
from loader import DB, DP


@DP.message_handler(Command('countallusers'), chat_id = admins_id)
async def all_users(msg: Message):
    count_users = DB.count_users()[0]
    await msg.answer(f"There is {count_users} users")

    del count_users
