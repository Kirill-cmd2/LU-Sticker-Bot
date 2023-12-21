from gino import Gino
from gino.schema import GinoSchemaVisitor

from config import PG_uri


db = Gino()

async def create_db():
    await db.set_bind(PG_uri)
    db.gino: GinoSchemaVisitor
    # await db.gino.drop_all() - delete everything
    # await db.gino.create_all()