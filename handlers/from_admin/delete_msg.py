from aiogram.dispatcher.filters.builtin import Command
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message

from config import admins_id
from loader import DP


@DP.message_handler(Command('delmsg', prefixes = '.'), chat_id = admins_id)
async def getting_chat_id(msg: Message, state: FSMContext):
    await state.update_data(chat_id = msg.text[8:])
    await state.set_state('wm_id')
    await msg.answer("Send me Message ID")


@DP.message_handler(state = 'wm_id')
async def deleting_msg(msg: Message, state: FSMContext):
    async with state.proxy() as data:
        user_id = data['chat_id']
    msg_id = int(msg.text)

    try:
        await DP.bot.delete_message(chat_id = user_id, message_id = msg_id)
        await msg.answer("I have delete it")
    except:
        await msg.answer("I could not delete it: something wrong in chat_id or msg_id")

    await state.finish()
