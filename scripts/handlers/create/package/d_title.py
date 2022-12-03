from aiogram.dispatcher import FSMContext
from aiogram.types import  Message

from loader import DP


@DP.message_handler(state = 'cnss_title')
async def cnss_title(msg:Message, state:FSMContext):
    await state.update_data(title = msg.text)
    await msg.answer("Stikerpak ssilkasi uchun ishlatiladigan nomni kiriting:\nP.S. Faqat lotin harflari ishlatilishi kerak! Raqamlarni ham ishlatish mumkin")
    await state.set_state('cnss_name')