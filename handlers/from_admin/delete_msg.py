from aiogram.dispatcher.filters.builtin import Command
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message
from aiogram.utils.exceptions import ChatNotFound, MessageToDeleteNotFound

from filters import IsAdminFilter
from loader import DP


@DP.message_handler(Command('delmsg', prefixes = '.'), IsAdminFilter())
async def delete_msg(msg: Message, state: FSMContext):
    """
    Function for deleting message

    chat_id: int - chat's id where message to be delete is located
    msg_id: int - id of message to be deleted
    """
    parts_of_msg = msg.text.split(' ')
    chat_id = int(parts_of_msg[1])
    msg_id = int(parts_of_msg[2])

    try:
        await DP.bot.delete_message(chat_id = chat_id, message_id = msg_id)
        await msg.answer("I have deleted it")

    except ChatNotFound:
        await msg.answer("Error: Chat not found!")

    except MessageToDeleteNotFound:
        await msg.answer("Error: Message to delete not found!")
