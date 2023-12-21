from aiogram.dispatcher.dispatcher import FSMContext
from aiogram.types import ContentType, Message

from config import admins_id, admin_and_user
from loader import BOT, DP


@DP.message_handler(state = 'sending_message', content_types = ContentType.ANY)
async def sending_message(msg:Message, state: FSMContext):
    user_id = admin_and_user[msg.from_user.id]

    hh = f'<a href="tg://user?id={user_id}">him/her</a>'
    admins_id.remove(msg.from_user.id)

# text, animation, audio, dice, document, sticker, photo, video

    if msg.content_type == ContentType.TEXT:
        sent_message = await BOT.send_message(chat_id = user_id, text = msg.text)

        for id in admins_id:
            await BOT.send_message(chat_id = id, text = f"Admin {msg.from_user.get_mention(as_html = True)} sent message below to {hh} Message and chat ID: {sent_message.message_id} {msg.chat.id}\n{msg.text}")

    elif msg.content_type == ContentType.ANIMATION:
        sent_message = await BOT.send_animation(chat_id = user_id, animation = msg.animation.file_id)

        for id in admins_id:
            await BOT.send_message(chat_id = id, text = f"Admin {msg.from_user.get_mention(as_html = True)} sent message below to {hh} Message and chat ID: {sent_message.message_id} {msg.chat.id}")
            await BOT.send_animation(chat_id = id, animation = msg.animation.file_id)

    elif msg.content_type == ContentType.AUDIO:
        sent_message = await BOT.send_audio(chat_id = user_id, audio = msg.audio.file_id)

        for id in admins_id:
            await BOT.send_message(chat_id = id, text = f"Admin {msg.from_user.get_mention(as_html = True)} sent message below to {hh} Message and chat ID: {sent_message.message_id} {msg.chat.id}")
            await BOT.send_audio(chat_id = id, audio = msg.audio.file_id)

    elif msg.content_type == ContentType.DICE:
        sent_message = await BOT.send_dice(chat_id = user_id, emoji = msg.dice.emoji)

        for id in admins_id:
            await BOT.send_message(chat_id = id, text = f"Admin {msg.from_user.get_mention(as_html = True)} sent message below to {hh} Message and chat ID: {sent_message.message_id} {msg.chat.id}")
            await BOT.send_dice(chat_id = id, emoji = msg.dice.emoji)

    elif msg.content_type == ContentType.DOCUMENT:
        sent_message = await BOT.send_document(chat_id = user_id, document = msg.document.file_id)

        for id in admins_id:
            await BOT.send_message(chat_id = id, text = f"Admin {msg.from_user.get_mention(as_html = True)} sent message below to {hh} Message and chat ID: {sent_message.message_id} {msg.chat.id}")
            await BOT.send_document(chat_id = id, document = msg.document.file_id)

    elif msg.content_type == ContentType.STICKER:
        sent_message = await BOT.send_sticker(chat_id = user_id, sticker = msg.sticker.file_id)

        for id in admins_id:
            await BOT.send_message(chat_id = id, text = f"Admin {msg.from_user.get_mention(as_html = True)} sent message below to {hh} Message and chat ID: {sent_message.message_id} {msg.chat.id}")
            await BOT.send_sticker(chat_id = id, sticker = msg.sticker.file_id)

    elif msg.content_type == ContentType.PHOTO:
        sent_message = await BOT.send_photo(chat_id = user_id, photo = msg.photo[-1].file_id)

        for id in admins_id:
            await BOT.send_message(chat_id = id, text = f"Admin {msg.from_user.get_mention(as_html = True)} sent message below to {hh} Message and chat ID: {sent_message.message_id} {msg.chat.id}")
            await BOT.send_photo(chat_id = id, photo = msg.photo[-1].file_id)

    elif msg.content_type == ContentType.VIDEO:
        sent_message = await BOT.send_video(chat_id = user_id, video = msg.video.file_id)

        for id in admins_id:
            await BOT.send_message(chat_id = id, text = f"Admin {msg.from_user.get_mention(as_html = True)} sent message below to {hh} Message and chat ID: {sent_message.message_id} {msg.chat.id}")
            await BOT.send_video(chat_id = id, video = msg.video.file_id)

    else:
        await msg.answer("I can not send this type of message")

    admins_id.append(msg.from_user.id)