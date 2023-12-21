from aiogram.dispatcher.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import Message
from aiogram.utils.exceptions import BotBlocked, ChatNotFound

from config import admin_and_user
from filters import IsAdminFilter
from loader import BOT, DP


@DP.message_handler(Command('sm', prefixes='.'), IsAdminFilter())
async def send_msg_to_user(msg: Message, state: FSMContext):
    userid = int(msg.text.split(' ')[1])

    try:
        await BOT.send_message(userid, "Admin Siz bilan suhbatni boshlamoqchi")
    
    except BotBlocked:
        await msg.answer("I was blocked by this user, so I can not send your message to the user")
    
    except ChatNotFound:
        await msg.answer("Error: Chat not found!")

    else:
        await state.set_state('sending_message')

    # admin_id: user_id
    admin_and_user[msg.from_user.id] = userid

    # user_id: admin_id
    admin_and_user[userid] = msg.from_user.id
