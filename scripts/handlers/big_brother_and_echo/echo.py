from aiogram.types import ContentType, Message

from config import admins_id
from loader import BOT, DP


@DP.message_handler(state="*")
async def echo_text(msg:Message):
    await msg.reply("Nima deb valdirayabsan-ey?!")
    for id in admins_id:
        try:
            await BOT.send_message(chat_id = id, text = f"{msg.text}\n{msg.from_user.full_name}dan\nIDsi: {msg.from_user.id}\nUsername: @{msg.from_user.username}")
        except:
            pass


@DP.message_handler(state="*", content_types=ContentType.DOCUMENT)
async def echo_doc(msg:Message):
    await msg.reply("Exo ishga tushdi!\n"
                        "Siz dokument yubordingiz. Uning IDsi:\n"+
                        msg.document.file_id)

    for id in admins_id:
        try:
            await BOT.send_document(chat_id=id, document=msg.document.file_id, caption=msg.from_user.full_name+"dan")
        except:
            pass


@DP.message_handler(state="*", content_types=ContentType.DICE)
async def echo_dice(msg:Message):
    await msg.reply("Mana Sizga!")
    await msg.answer_dice(msg.text)

    for id in admins_id:
        try:
            await BOT.send_dice(chat_id=id, emoji=msg.text)
            await BOT.send_message(chat_id=id, text=msg.from_user.full_name+"dan")
        except:
            pass

@DP.message_handler(state="*", content_types=ContentType.STICKER)
async def echo_sticker(msg:Message):
    await msg.reply(f"Exo ishga tushdi!\n"
                     f"Siz STIKER yubordingiz. Uning IDsi:\n"+
                     msg.sticker.file_id)
    for id in admins_id:
        try:
            await BOT.send_sticker(chat_id=id, sticker=msg.sticker.file_id)
            await BOT.send_message(chat_id=id, text=msg.from_user.full_name+"dan")
        except:
            pass

@DP.message_handler(state="*", content_types=ContentType.PHOTO)
async def echo_photo(msg:Message):
    await msg.reply(f"Exo ishga tushdi!\n"
                     f"Siz RASM yubordingiz. Uning IDsi:\n"+
                     msg.photo[-1].file_id)
    for id in admins_id:
        try:
            await BOT.send_photo(chat_id=id, photo=msg.photo[-1].file_id, caption=msg.from_user.full_name+"dan")
        except:
            pass

@DP.message_handler(state="*", content_types=ContentType.VIDEO)
async def echo_video(msg:Message):
    await msg.reply(f"Exo ishga tushdi!\n"
                     f"Siz VIDEO yubordingiz. Uning IDsi:\n"+
                     msg.video.file_id)
    for id in admins_id:
        try:
            await BOT.send_video(chat_id=id, video=msg.video.file_id, caption=msg.from_user.full_name+"dan")
        except:
            pass

@DP.message_handler(state="*", content_types=ContentType.AUDIO)
async def echo_audio(msg:Message):
    await msg.reply(f"Exo ishga tushdi!\n"
                     f"Siz OVOZLI XABAR yubordingiz. Uning IDsi:\n"+
                     msg.audio.file_id)
    for id in admins_id:
        try:
            await BOT.send_audio(chat_id=id, audio=msg.audio.file_id, caption=msg.from_user.full_name+"dan")
        except:
            pass

@DP.message_handler(state="*", content_types=ContentType.ANIMATION)
async def echo_animation(msg:Message):
    await msg.reply(f"Exo ishga tushdi!\n"
                     f"Siz GIF yubordingiz. Uning IDsi:\n"+
                     msg.animation.file_id)
    for id in admins_id:
        try:
            await BOT.send_animation(chat_id=id, animation=msg.animation.file_id, caption=msg.from_user.full_name+"dan")
        except:
            pass
