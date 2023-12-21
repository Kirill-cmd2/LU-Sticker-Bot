from sqlalchemy import sql, Column, Integer

from create_db import db


class User(db.Model):
    __tablename__ = 'Users'
    query: sql.Select

    user_id = Column(Integer, primary_key=True)
    stickerpacks = 