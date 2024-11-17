from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType, Message

from loader import DP
from utils import cnssStates


@DP.message_handler(state = cnssStates.cnss_title)
async def cnss_title(msg:Message, state:FSMContext):
    await state.update_data(title = msg.text)
    await msg.answer("Stikerpak ssilkasi uchun ishlatiladigan nomni kiriting:\n\nP.S. Faqat lotin harflari va raqamlar ishlatilishi kerak! Birinchi belgi lotin harfi bo'lishi shart.")

    await cnssStates.cnss_name.set()


@DP.message_handler(state = cnssStates.cnss_title, content_types=ContentType.ANY)
async def wrong_title(msg:Message):
    await msg.answer("Iltimos, stikerpakingizga nom o'ylab topib kiriting")