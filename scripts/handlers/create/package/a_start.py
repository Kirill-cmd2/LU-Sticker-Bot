from aiogram.dispatcher.storage import FSMContext
from aiogram.types import CallbackQuery

from loader import DP


@DP.callback_query_handler(text = 'new:set')
async def ansts_start(cq:CallbackQuery, state:FSMContext):
    await cq.answer("Mayli, yaratamiz!👌🏻")
    await cq.message.answer("Rasm yuboring-chi!🏞")
    await state.set_state('cnss_photo')


@DP.callback_query_handler(text = 'new:set', state = '*')
async def cancel_caching(cq:CallbackQuery):
    await cq.answer(cache_time = 10)
