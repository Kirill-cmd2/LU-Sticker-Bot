from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message

from ....filters import IsEmojiFilter
from loader import DP

from .e_finish import finish


@DP.message_handler(IsEmojiFilter(), state = 'ansts_emoji')
async def ansts_emoji(msg:Message, state:FSMContext):
    await msg.answer_chat_action('typing')
    await state.update_data(emoji = msg.text)
    await finish(m = msg, s = state)