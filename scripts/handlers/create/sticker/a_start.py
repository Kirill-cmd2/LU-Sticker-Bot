from aiogram.dispatcher.storage import FSMContext
from aiogram.types import CallbackQuery

from loader import DP


@DP.callback_query_handler(text = 'new:sticker')
async def ansts_start(cq: CallbackQuery, state: FSMContext):
    await cq.answer("'Boriga Baraka' qatnashchilari aytardi: Qo'shing!")
    await cq.message.answer("Stikerpak ssilkasi uchun ishlatilgan nomni kiriting:")
    await state.set_state('ansts_name')


@DP.callback_query_handler(text = 'new:sticker', state = '*')
async def cancel_caching(cq: CallbackQuery):
    await cq.answer(cache_time = 10)
