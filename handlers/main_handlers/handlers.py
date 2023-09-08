from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command, CommandHelp, CommandStart
from aiogram.types import Message, ReplyKeyboardRemove

from loader import DP
from utils import rate_limit, stick, set_default_commands_with_language_code


@rate_limit(10, 'start')
@DP.message_handler(CommandStart(), state='*')
async def start(msg: Message, state: FSMContext):
    await state.finish()
    await msg.answer_sticker('CAACAgIAAxkBAAECoXlg_OYUFgPxhnc0CLO0epNhI8hPoQACJQADns6VGgABEDLTUjOmQyAE')
    await msg.answer(text = f"Salom, {msg.from_user.first_name}!\nNima qilay, xo'jayin?\nPastdagi tugmachalardan foydalaning!",
        reply_markup = stick)

    # await set_default_commands_with_language_code(DP.bot, msg.chat.id)


@rate_limit(10, 'menu')
@DP.message_handler(Command('menu'))
async def menu(msg: Message, state: FSMContext):
    await state.finish()
    await msg.answer("Tanlang-tanlang. Barchasini bajaraman!\nPastdagi tugmachalardan foydalaning!", reply_markup = stick)


@rate_limit(10, 'help')
@DP.message_handler(CommandHelp())
async def help(msg: Message):
    text="Ushbu Telegram Bot rasmlaringizni stikerlarga aylantirish uchun yaratilgan\n\
Yangi stikerpak - stikerlar to'plamini yarating va unga birinchi stikeringzni qo'shing\n\
Yangi stiker - stikerpakingiz bor bo'lsa, unga yangi stiker qo'shing\n\
Stikerni o'chirish - stikeringizni o'chirmoqchi bo'lsangiz\n\n\
Dasturlash tili: Python 3.8.10\n\
Ishlatilgan kutubxonalar: aiogram 2.23.1   Pillow 7.0.0\n\n\
Xatoliklarga duch kelsangiz, iltimos, @lu_main_admin'ga murojaat qiling!"
    await msg.answer(text)


@rate_limit(5, 'cancel')
@DP.message_handler(Command('cancel'), state='*')
async def cancel(msg: Message, state: FSMContext):
    name_of_state = await state.get_state()

    text = "Bekor qilindi"

    if name_of_state:
        if name_of_state.__contains__('cnss'):
            text = "Stikerpak yaratilishi bekor qilindi"
        elif name_of_state.__contains__('ansts'):
            text = "Yangi stiker yaratilishi bekor qilindi"
        elif name_of_state.__contains__('del'):
            text = "Stiker o'chirilishi bekor qilindi"
    else:
        text = "Bekor qilindi"

    await msg.reply(text, reply_markup = ReplyKeyboardRemove())

    await state.finish()
