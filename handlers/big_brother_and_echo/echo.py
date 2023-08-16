from aiogram.dispatcher.storage import FSMContext
from aiogram.types import ContentType, Message

from loader import DP
from utils import writing_logs


@DP.message_handler(state="*")
async def echo_text(msg:Message, state:FSMContext):
    user_state = await state.get_state()
    await writing_logs(msg.chat.id, f"State: {user_state} - {msg.text}")


@DP.message_handler(state="*", content_types=ContentType.DOCUMENT)
async def echo_doc(msg:Message):
    await msg.reply("Echo activated!\n"
                        "You sent the document. It's ID:\n"
                        f"<code>{msg.document.file_id}</code>")

    await writing_logs(msg.chat.id, f"Document's ID: {msg.document.file_id}")


@DP.message_handler(state="*", content_types=ContentType.DICE)
async def echo_dice(msg:Message):
    await msg.reply("Catch mine!")
    await msg.answer_dice(msg.text)

    await writing_logs(msg.chat.id, f"Dice - {msg.text}")


@DP.message_handler(state="*", content_types=ContentType.STICKER)
async def echo_sticker(msg:Message):
    await msg.reply(f"Exo ishga tushdi!\n"
                     f"Siz STIKER yubordingiz. Uning IDsi:\n"
                     f"<code>{msg.sticker.file_id}</code>")

    await writing_logs(msg.chat.id, f"Sticker's ID: {msg.sticker.file_id}")


@DP.message_handler(state="*", content_types=ContentType.PHOTO)
async def echo_photo(msg:Message):
    await msg.reply(f"Exo ishga tushdi!\n"
                     f"Siz RASM yubordingiz. Uning IDsi:\n"
                     f"<code>{msg.photo[-1].file_id}</code>")

    await writing_logs(msg.chat.id, f"Photo's ID: {msg.photo[-1].file_id}")


@DP.message_handler(state="*", content_types=ContentType.VIDEO)
async def echo_video(msg:Message):
    await msg.reply(f"Exo ishga tushdi!\n"
                     f"Siz VIDEO yubordingiz. Uning IDsi:\n"
                     f"<code>{msg.video.file_id}</code>")

    await writing_logs(msg.chat.id, f"Video's ID: {msg.video.file_id}")


@DP.message_handler(state="*", content_types=ContentType.AUDIO)
async def echo_audio(msg:Message):
    await msg.reply(f"Exo ishga tushdi!\n"
                     f"Siz OVOZLI XABAR yubordingiz. Uning IDsi:\n"
                     f"<code>{msg.audio.file_id}</code>")

    await writing_logs(msg.chat.id, f"Audio's ID: {msg.audio.file_id}")


@DP.message_handler(state="*", content_types=ContentType.ANIMATION)
async def echo_animation(msg:Message):
    await msg.reply(f"Exo ishga tushdi!\n"
                     f"Siz GIF yubordingiz. Uning IDsi:\n"
                     f"<code>{msg.animation.file_id}</code>")

    await writing_logs(msg.chat.id, f"Animation's ID: {msg.animation.file_id}")
