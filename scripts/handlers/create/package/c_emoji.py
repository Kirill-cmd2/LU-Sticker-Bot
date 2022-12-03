from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from ....filters import IsEmojiFilter
from loader import DP


@DP.message_handler(IsEmojiFilter(), state='cnss_emoji')
async def cnss_emoji(msg:Message, state:FSMContext):
    await state.update_data(emoji = msg.text)
    await msg.answer("Endi stikerpak ismini yuboring")
    await state.set_state('cnss_title')