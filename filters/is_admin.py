from aiogram.dispatcher.filters import BoundFilter
from aiogram.types.message import Message

from config import admins_id


class IsAdminFilter(BoundFilter):
    def __init__(self) -> None:
        super().__init__()
    
    async def check(self, msg: Message) -> bool:
        return True if msg.from_user.id in admins_id else False