from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


cdf_creating = CallbackData('new', 'what_is_it')
cdf_deleting = CallbackData('del', 'what')

stick = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌌 Yangi stikerpak 🌌", callback_data = cdf_creating.new(what_is_it='set')),
            InlineKeyboardButton(text="🎆 Yangi stiker 🎆", callback_data = 'new:sticker')
        ],
        [
            InlineKeyboardButton(text="🗑 Stikerni o'chirish 🗑", callback_data='del:sticker')
        ]
    ],
    row_width=2,
)
