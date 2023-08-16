from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command, CommandHelp, CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
from sqlite3.dbapi2 import IntegrityError

from loader import DB, DP
from utils import creating_mention, rate_limit, stick, writing_logs, set_default_commands_with_language_code


@rate_limit(10, 'start')
@DP.message_handler(CommandStart(), state='*')
async def start(msg: Message, state: FSMContext):
    await state.finish()
    await msg.answer_sticker('CAACAgIAAxkBAAECoXlg_OYUFgPxhnc0CLO0epNhI8hPoQACJQADns6VGgABEDLTUjOmQyAE')
    await msg.answer(text = f"Salom, {msg.from_user.first_name}!\nNima qilay, xo'jayin?\nPastdagi tugmachalardan foydalaning!",
        reply_markup = stick)

    # await set_default_commands_with_language_code(DP.bot, msg.chat.id)

    # await writing_logs(msg.chat.id, f"{msg.from_user.id} pressed the /start button")

    # try:
    #     DB.add_user(id = msg.from_user.id, name = msg.from_user.full_name)
    # except IntegrityError as err:
    #     print(err)# - send to admin

    # sending to admin the mention of a user in inline button
    # await creating_mention(msg, f"{msg.from_user.full_name} pressed start\n{msg.from_user.id}")


@rate_limit(10, 'menu')
@DP.message_handler(Command('menu'))
async def menu(msg: Message, state: FSMContext):
    await state.finish()
    await msg.answer("Tanlang-tanlang. Barchasini bajaraman!\nPastdagi tugmachalardan foydalaning!", reply_markup = stick)


# @DP.message_handler(Command('goback'))
# async def going_to_previous_handler(msg: Message, state: FSMContext):
#     await state

#add goback command to set_default_commands 


@rate_limit(10, 'help')
@DP.message_handler(CommandHelp())
async def help(msg: Message):
    await msg.answer("Ushbu Telegram Bot rasmlaringizni stikerlarga aylantirish uchun yaratilgan\n\
Yangi stikerpak - stikerlar to'plamini yarating va unga birinchi stikeringzni qo'shing\n\
Yangi stiker - stikerpakingiz bor bo'lsa, unga yangi stiker qo'shing\n\
Stikerni o'chirish - stikeringizni o'chirmoqchi bo'lsangiz\n\n\
Dasturlash tili: Python 3.8.10\n\
Ishlatilgan kutubxonalar: aiogram 2.23.1   Pillow 7.0.0\n\n\
Xatoliklarga duch kelsangiz, iltimos, @lu_main_admin'ga murojaat qiling!")


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
    del name_of_state, text
    await state.finish()
