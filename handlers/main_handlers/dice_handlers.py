from asyncio import sleep
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Text
from aiogram.types import Message, ContentType
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from random import choice
from config import admins_id
from loader import DP as dp, BOT as bot

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


playi=ReplyKeyboardMarkup(keyboard=[[KeyboardButton("Qani, boshla o'yinni! 💪")],],resize_keyboard=True)

yana_play=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Yana o'yin! 🤪")],
        [KeyboardButton("To'xtat! Yetar endi?! 😐")],
        ], resize_keyboard=True)


@dp.message_handler(commands=["start"])
async def start_message(message: Message):
    await dp.bot.send_sticker(chat_id=message.from_user.id, sticker='CAACAgIAAxkBAAECoXlg_OYUFgPxhnc0CLO0epNhI8hPoQACJQADns6VGgABEDLTUjOmQyAE')
    await dp.bot.send_message(chat_id=message.from_user.id, text=f"Salom {message.from_user.full_name}👋!\nKeling, o'yin o'ynaymiz!😁",\
        reply_markup=playi)


@dp.message_handler(commands=["play_dice"])
@dp.message_handler(Text(equals="Qani, boshla o'yinni! 💪"))
@dp.message_handler(Text(equals="Yana o'yin! 🤪"))
async def play(message:Message, state:FSMContext):
    dice = ['🎲','🎰','🎯','🏀','⚽','🎳']
    
    bot_data=await bot.send_dice(chat_id=message.from_user.id, emoji=choice(dice), reply_markup=ReplyKeyboardRemove())

    async with state.proxy() as data:
        data['bot_dice_num']=bot_data['dice']['value']

    await sleep(7)
    await bot.send_message(message.from_user.id, "Endi esa yuqoridagidan siz yuboring...⏰")
    
    for id in admins_id:
        await bot.send_message(chat_id=id, text=f"{message.from_user.full_name} botda o'ynashni bosdi.\
            \nID: {message.from_user.id}\
            \nUsername: {message.from_user.username}")


@dp.message_handler(content_types=ContentType.DICE)
async def catch_user_dice(message:Message, state:FSMContext):
    user_dice_num=message.dice.value

    async with state.proxy() as data:
        bot_dice_num=data['bot_dice_num']

    await sleep(6)

    if bot_dice_num<user_dice_num:
        await bot.send_sticker(chat_id=message.from_user.id, sticker='CAACAgIAAxkBAAEC_a1hVdOgvCMQyIuS5zFMncdt3LrlbAACdxMAApXxxgaYkX27gSoMgCEE')
        await bot.send_message(message.from_user.id, f"Menda {bot_dice_num}, sizda esa {user_dice_num}\
            \n{message.from_user.first_name}, Siz dahosiz! 🙈\nYangidan! G'irromchilik bo'ldi! Hakermisiz nima balo?!",\
            reply_markup=yana_play)

    elif bot_dice_num>user_dice_num:
        await bot.send_message(message.from_user.id, f"Menda {bot_dice_num}, sizda esa {user_dice_num}\
            \nMen yutdim! Dunyoni egallashimga ozgina qoldi...🙊\n Hammasi haqqoniy! Botlar baribir zo'r-da!",\
            reply_markup=yana_play)
        await bot.send_sticker(chat_id=message.from_user.id, sticker='CAACAgQAAxkBAAEC_a9hVdPlxowMKuhgoIJhWD5unDNqtAAC_BYAAqbxcR5VXkg8yvhuVCEE')

    else:
        await bot.send_message(message.from_user.id, f"Menda {bot_dice_num}, sizda ham {user_dice_num}\
            \nIkkalamiz ham yutdik! {message.from_user.first_name}dek kuchli odam ko'rmaganman🐵!", \
            reply_markup=yana_play)
        await bot.send_sticker(chat_id=message.from_user.id, sticker='CAACAgIAAxkBAAEC_bFhVdQv6BNKk-jCG8UVSGDNdSwkYwACJgADns6VGkYqM-f5PsjXIQQ')

    await state.finish()


@dp.message_handler(Text(equals="To'xtat! Yetar endi?! 😐"))
async def cancel(msg:Message):
    #await bot.send_audio(chat_id=msg.from_user.id, audio=1, reply_markup=ReplyKeyboardRemove())
    await bot.send_message(chat_id=msg.from_user.id, text="Yaxshi! To'xtatamiz!!! 😳", reply_markup=ReplyKeyboardRemove())
