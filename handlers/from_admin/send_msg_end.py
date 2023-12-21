from aiogram.dispatcher.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import Message

from config import admin_and_user
from loader import BOT, DP


@DP.message_handler(Command('esm', prefixes='.'), state = 'sending_message')
async def end_sending_msg(msg: Message, state: FSMContext):
    user_id = admin_and_user[msg.from_user.id]
    
    await BOT.send_message(user_id, "Admin Siz bilan suhbatni tugatdi")

    del admin_and_user[msg.from_user.id], admin_and_user[user_id]
    await state.finish()