from aiogram.dispatcher.filters.builtin import Command
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message

from loader import DP


@DP.message_handler(Command('delmsg'))
async def waiting_user_id(msg: Message, state: FSMContext):
    await state.set_state('wc_id')
    await msg.answer("Send me Chat ID")

    
@DP.message_handler(state = 'wc_id')
async def waiting_user_id(msg: Message, state: FSMContext):
    await state.update_data(chat_id = msg.text)
    await state.set_state('wm_id')
    await msg.answer("Send me Message ID")


@DP.message_handler(state = 'wm_id')
async def waiting_msg_id(msg: Message, state: FSMContext):
    async with state.proxy() as data:
        user_id = data['chat_id']
    msg_id = msg.text

    await state.finish()

    await DP.bot.delete_message(chat_id = user_id, message_id = msg_id)
    await msg.answer("I have delete it")

    del user_id, msg_id