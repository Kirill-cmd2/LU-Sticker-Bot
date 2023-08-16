from aiogram.types import CallbackQuery

from loader import DP
from utils import cnssStates, anstsStates, delstickerStates


# cancelling same pushes to inline buttons
@DP.callback_query_handler(text = 'new:set', state = cnssStates.cnss_photo)
@DP.callback_query_handler(text = 'new:sticker', state = anstsStates.ansts_name)
@DP.callback_query_handler(text = 'del:sticker', state = delstickerStates.delstick)
async def cancel_same_callback(cq:CallbackQuery):
    await cq.answer(cache_time = 5)
    return


# creating a package
@DP.callback_query_handler(text = 'new:set', state = '*')
async def cnss_start(cq:CallbackQuery):
    await cq.answer("Mayli, yaratamiz!👌🏻")
    await cq.message.answer("Rasm yuboring-chi!🏞")

    await cnssStates.cnss_photo.set() # it goes to create -> package -> b_photo.py

    await cq.answer(cache_time = 5)


# creating a sticker
@DP.callback_query_handler(text = 'new:sticker', state='*')
async def ansts_start(cq: CallbackQuery):
    await cq.answer("'Boriga Baraka' qatnashchilari aytardi: Qo'shing!")
    await cq.message.answer("Stikerpak ssilkasi uchun ishlatilgan nomni kiriting:")

    await anstsStates.ansts_name.set() # it goes to create -> sticker -> b_name.py

    await cq.answer(cache_time=5)


# deleting a sticker
@DP.callback_query_handler(text = 'del:sticker', state='*')
async def wait_del_stick(cq:CallbackQuery):
    await cq.answer("Yubo-o-o-r!")
    await cq.message.answer("Qaysi stikerni o'chirmoqchi bo'lsangiz shuni yuboring\nBu stiker sizga tegishli va aynan shu bot yordamida yaratilgan bo'lishi kerak\n/cancel - Bekor qilish")

    await delstickerStates.delstick.set() # goes to handlers -> delete -> sticker.py

    await cq.answer(cache_time = 5)
