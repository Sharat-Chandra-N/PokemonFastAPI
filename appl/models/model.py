from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from ..database.database import Base


class Pokemon(Base):
    __tablename__ = "pokemon"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150))
    birth_date = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )


class Owner(Base):
    __tablename__ = "owner"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150))
    gym = Column(String(150))


class Country(Base):
    __tablename__ = "country"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150))


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150))


class Review(Base):
    __tablename__ = "review"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(250))
    text = Column(String(350))


class Reviewer(Base):
    __tablename__ = "reviewer"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(150))
    last_name = Column(String(150))
