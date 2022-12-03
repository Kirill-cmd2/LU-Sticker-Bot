from aiogram.dispatcher.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import ContentType, Message
from aiogram.utils.exceptions import BotBlocked

from config import admins_id
from loader import DP, BOT


@DP.message_handler(text = '.', chat_id = admins_id)
async def send_msg_to_user(msg: Message, state: FSMContext):
    await state.finish()
    await state.set_state('wsmfa')


@DP.message_handler(state = 'wsmfa')
async def wsmfa(msg: Message, state: FSMContext):
    await state.update_data(user_id = msg.text)
    await state.set_state('send_message')


@DP.message_handler(state = 'send_message', content_types = ContentType.ANY)
async def sending_message(msg:Message, state: FSMContext):
    async with state.proxy() as data:
        user_id = data['user_id']

    try:
# text, animation, audio, dice, document, sticker, photo, video

        if msg.content_type == ContentType.TEXT:
            await BOT.send_message(chat_id = user_id, text = msg.text)

        elif msg.content_type == ContentType.ANIMATION:
            await BOT.send_animation(chat_id = user_id, animation = msg.animation.file_id)

        elif msg.content_type == ContentType.AUDIO:
            await BOT.send_audio(chat_id = user_id, audio = msg.audio.file_id)

        elif msg.content_type == ContentType.DICE:
            await BOT.send_dice(chat_id = user_id, emoji = msg.dice.emoji)

        elif msg.content_type == ContentType.DOCUMENT:
            await BOT.send_document(chat_id = user_id, document = msg.document.file_id)

        elif msg.content_type == ContentType.STICKER:
            await BOT.send_sticker(chat_id = user_id, sticker = msg.sticker.file_id)

        elif msg.content_type == ContentType.PHOTO:
            await BOT.send_photo(chat_id = user_id, photo = msg.photo[-1].file_id)

        elif msg.content_type == ContentType.VIDEO:
            await BOT.send_video(chat_id = user_id, video = msg.video.file_id)
        
        else:
            await msg.answer("I can not send this type of message")

    except BotBlocked:
        msg.answer("I was blocked by this user, so I can not send your message to the user")

    del user_id
