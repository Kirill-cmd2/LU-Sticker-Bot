from loader import DP

from .throttling import ThrottlingMiddleware
#from aiogram.contrib.middlewares.logging import LoggingMiddleware


if __name__ == "middlewares":
    DP.middleware.setup(ThrottlingMiddleware())
    #DP.middleware.setup(LoggingMiddleware())
