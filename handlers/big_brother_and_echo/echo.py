from aiogram.types import ContentType, Message

from loader import DP


@DP.message_handler(state="*", content_types=ContentType.DOCUMENT)
async def echo_doc(msg:Message):
    await msg.reply("Echo activated!\n"
                        "You sent the document. It's ID:\n"
                        f"<code>{msg.document.file_id}</code>")


@DP.message_handler(state="*", content_types=ContentType.DICE)
async def echo_dice(msg:Message):
    await msg.reply("Catch mine!")
    await msg.answer_dice(msg.text)


@DP.message_handler(state="*", content_types=ContentType.STICKER)
async def echo_sticker(msg:Message):
    await msg.reply(f"Exo ishga tushdi!\n"
                     f"Siz STIKER yubordingiz. Uning IDsi:\n"
                     f"<code>{msg.sticker.file_id}</code>")


@DP.message_handler(state="*", content_types=ContentType.PHOTO)
async def echo_photo(msg:Message):
    await msg.reply(f"Exo ishga tushdi!\n"
                     f"Siz RASM yubordingiz. Uning IDsi:\n"
                     f"<code>{msg.photo[-1].file_id}</code>")


@DP.message_handler(state="*", content_types=ContentType.VIDEO)
async def echo_video(msg:Message):
    await msg.reply(f"Exo ishga tushdi!\n"
                     f"Siz VIDEO yubordingiz. Uning IDsi:\n"
                     f"<code>{msg.video.file_id}</code>")


@DP.message_handler(state="*", content_types=ContentType.AUDIO)
async def echo_audio(msg:Message):
    await msg.reply(f"Exo ishga tushdi!\n"
                     f"Siz OVOZLI XABAR yubordingiz. Uning IDsi:\n"
                     f"<code>{msg.audio.file_id}</code>")


@DP.message_handler(state="*", content_types=ContentType.ANIMATION)
async def echo_animation(msg:Message):
    await msg.reply(f"Exo ishga tushdi!\n"
                     f"Siz GIF yubordingiz. Uning IDsi:\n"
                     f"<code>{msg.animation.file_id}</code>")
