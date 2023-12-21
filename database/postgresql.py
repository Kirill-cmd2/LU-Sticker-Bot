from asyncio import AbstractEventLoop, get_event_loop
from asyncpg import create_pool, exceptions, pool

# import config
ip = 'localhost'
PGuser = 'StickBotDatabase'
PGpassword = 'postgres'


class StickBotDatabase:
    def __init__(self, loop: AbstractEventLoop):
        self.pool: pool.Pool = loop.run_until_complete(
            create_pool(
                user = PGuser,
                password = PGpassword,
                host = ip
            )
        )
    
    async def create_table_users(self):
        sql = """
CREATE TABLE IF NOT EXISTS Users (
id INT NOT NULL,
lan VARCHAR(2),
username VARCHAR(64),
PRIMARY KEY (id)
)
"""
        await self.pool.execute(sql)
    
    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}"
            for num, item in enumerate(parameters, start=1)
        ])
        return sql, tuple(parameters.values())
    
    async def add_user(self, id: int, username: str):
        sql = "INSERT INTO Users (id, username) VALUES ($1, $2)"
        try:
            await self.pool.execute(sql, id, username)
        except exceptions.UniqueViolationError:
            pass
    
    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.pool.fetch(sql)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return await self.pool.fetchrow(sql, *parameters)

    async def count_users(self):
        return await self.pool.fetchval("SELECT COUNT(*) FROM Users")
    
    async def update_user_username(self, id, username):
        sql = "UPDATE Users SET username = $1 WHERE id = $2"
        return await self.pool.execute(sql, username, id)
    
    async def delete_user(self, id):
        sql = "DELETE FROM Users WHERE id = $1"
        await self.pool.execute(sql, id)

    async def delete_all_users(self):
        await self.pool.execute("DELETE FROM Users WHERE True")


# check connection to database
db = StickBotDatabase(loop=get_event_loop())