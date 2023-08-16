from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeChat


async def set_default_commands_with_language_code(bot: Bot, chat_id: int):
    commands_for_language_code = {
    'uz': [
        BotCommand('start', "Botni ishga tushirish"),
        BotCommand('menu', "Menyu"),
        BotCommand('help', "Qo'shimcha ma'lumot"),
        BotCommand('cancel', "Barchasini bekor qilish")
    ],
    'en': [
        BotCommand('start', "Starting bot"),
        BotCommand('menu', "Menu"),
        BotCommand('help', "Additional information"),
        BotCommand('cancel', "Cancel everything")
    ],
    'ru': [
        BotCommand('start', "Запустить бота"),
        BotCommand('menu', "Меню"),
        BotCommand('help', "Дополнительная информация"),
        BotCommand('cancel', "Отменить всё")
    ]
}
    for lan_code, command in commands_for_language_code.items():
        await bot.set_my_commands(
            commands = command,
            scope = BotCommandScopeChat(chat_id),
            language_code = lan_code
        )
