from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message

from filters import IsEmojiFilter
from loader import DP
from utils import anstsStates

from .e_finish import finish


@DP.message_handler(IsEmojiFilter(), state = anstsStates.ansts_emoji)
async def ansts_emoji(msg:Message, state:FSMContext, emoji_list):
    await msg.answer_chat_action('typing')
    await state.update_data(emoji = emoji_list)

    await finish(m = msg, s = state)


@DP.message_handler(state = anstsStates.ansts_emoji)
async def wrong_emoji(msg:Message):
    await msg.answer("Iltimos, boshqa EMOJI yuboring!\n\nYoki to'xtating /cancel")
