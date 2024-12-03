from loader import DP

from .throttling import ThrottlingMiddleware


if __name__ == "middlewares":
    DP.middleware.setup(ThrottlingMiddleware())
