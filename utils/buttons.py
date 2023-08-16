from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


stick = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌌 Yangi stikerpak 🌌", callback_data = 'new:set'),
            InlineKeyboardButton(text="🎆 Yangi stiker 🎆", callback_data = 'new:sticker')
        ],
        [
            InlineKeyboardButton(text="🗑 Stikerni o'chirish 🗑", callback_data='del:sticker')
        ],
        [
            InlineKeyboardButton(text="Bekor qilish", callback_data='cancel')
        ]
    ],
    row_width=2,
)
