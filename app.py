from aiogram import Dispatcher
from loader import DP
import middlewares, filters, handlers


async def shutdown(DP: Dispatcher):
    await DP.storage.close()
    await DP.storage.wait_closed()


if __name__ == "__main__":
    from aiogram.utils.executor import start_polling
    start_polling(dispatcher = DP,
                on_shutdown = shutdown,
                skip_updates = True)


__version__ = '2.1.8'
