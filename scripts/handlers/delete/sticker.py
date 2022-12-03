from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ContentType, Message

from loader import DP
from ...utils import stick


@DP.callback_query_handler(text = 'del:sticker')
async def wait_del_stick(cq:CallbackQuery, state:FSMContext):
    await cq.answer("Yubo-o-o-r!")
    await cq.message.answer("Qaysi stikerni o'chirmoqchi bo'lsangiz shuni yuboring\nBu stiker sizga tegishli va aynan shu bot yordamida yaratilgan bo'lishi kerak\n/cancel - Bekor qilish")
    await state.set_state('delstick')

@DP.message_handler(state = 'delstick', content_types = ContentType.STICKER)
async def del_stick(msg:Message, state:FSMContext):
    await state.finish()

    try:
        await msg.sticker.delete_from_set()
        await msg.reply("O'chirib, yo'q qilib yubordim!")

    except Exception:
        await msg.answer("Xatolik yuz berdi! Iltimos, qaytadan urinib ko'ring",
            reply_markup = stick)


@DP.callback_query_handler(text = 'del:sticker', state = '*')
async def cancel_cache(cq: CallbackQuery):
    await cq.answer(cache_time = 10)