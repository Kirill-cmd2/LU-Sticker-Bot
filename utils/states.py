from aiogram.dispatcher.filters.state import State, StatesGroup

# create new sticker set States
class cnssStates(StatesGroup):
    cnss_photo = State()
    cnss_emoji = State()
    cnss_title = State()
    cnss_name = State()

# add new sticker to set States
class anstsStates(StatesGroup):
    ansts_name = State()
    ansts_photo = State()
    ansts_emoji = State()

# delete sticker States
class delstickerStates(StatesGroup):
    delstick = State()

# wait user ids
class waitIDs(StatesGroup):
    waitids = State()
