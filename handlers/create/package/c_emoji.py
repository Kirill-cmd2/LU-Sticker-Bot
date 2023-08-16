from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentType

from filters import IsEmojiFilter
from loader import DP
from utils import cnssStates


@DP.message_handler(IsEmojiFilter(), state=cnssStates.cnss_emoji)
async def cnss_emoji(msg:Message, state:FSMContext, emoji_list):
    await state.update_data(emoji = emoji_list)
    await msg.answer("Endi stikerpak ismini yuboring")

    await cnssStates.cnss_title.set()


@DP.message_handler(state=cnssStates.cnss_emoji, content_types=ContentType.ANY)
async def wrong_emoji(msg:Message):
    await msg.answer("Iltimos, EMOJI yuboring!\n\nYoki to'xtating /cancel")
