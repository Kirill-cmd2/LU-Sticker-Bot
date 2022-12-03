from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardRemove

from config import admins_id
from loader import DP
from ...utils import rate_limit, stick


@rate_limit(10, 'start')
@DP.message_handler(CommandStart(), state='*')
async def start(msg: Message, state: FSMContext):
    await state.finish()
    await msg.answer_sticker('CAACAgIAAxkBAAECoXlg_OYUFgPxhnc0CLO0epNhI8hPoQACJQADns6VGgABEDLTUjOmQyAE')
    await msg.answer(text = f"Salom, {msg.from_user.first_name}!\nNima qilay, xo'jayin?\nPastdagi tugmachalardan foydalaning!",
        reply_markup = stick)
    for id in admins_id:
        try:
            await DP.bot.send_message(chat_id = id, text = f"{msg.from_user.get_mention(as_html = True)}\n{msg.from_user.full_name} Startni bosdi\nIDsi: {msg.from_user.id}\nUsername: @{msg.from_user.username}")
        except:
            pass


@rate_limit(10, 'menu')
@DP.message_handler(Command('menu'))
async def menu(msg: Message, state: FSMContext):
    await state.finish()
    await msg.answer("Tanlang-tanlang. Barchasini bajaraman!\nPastdagi tugmachalardan foydalaning!", reply_markup = stick)


@rate_limit(10, 'help')
@DP.message_handler(Command('help'))
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

    if name_of_state == None:
        await msg.reply(text = "Bekor qilindi", reply_markup = ReplyKeyboardRemove())
    elif name_of_state.__contains__('cnss'):
        await msg.reply(text = "Stikerpak yaratilishi bekor qilindi", reply_markup = ReplyKeyboardRemove())
    elif name_of_state.__contains__('ansts'):
        await msg.reply(text = "Yangi stiker yaratilishi bekor qilindi", reply_markup = ReplyKeyboardRemove())


    await state.finish()