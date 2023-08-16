from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.storage import FSMContext

from loader import DP
from utils import waitIDs


@DP.message_handler(Command('sendlog'))
async def wait_user_id(msg:Message):
    await msg.answer("Send user's ID")
    await waitIDs.waitids.set()


@DP.message_handler(state=waitIDs.waitids)
async def wait_user_id(msg:Message, state:FSMContext):
    try:
        await msg.answer_document()
    except:
        pass