from loader import DP
from scripts import middlewares, filters, handlers

__version__ = '2.0.0'

async def shutdown(DP):
    await DP.storage.close()
    await DP.storage.wait_closed()


if __name__ == "__main__":
    from aiogram.utils.executor import start_polling
    start_polling(dispatcher = DP,
                on_shutdown = shutdown,
                skip_updates = True)
