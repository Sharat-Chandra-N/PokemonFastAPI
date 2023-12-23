from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
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
    category_id = Column(ForeignKey("category.id", ondelete="CASCADE"), nullable=False)
    category = relationship("Category")
    reviews = relationship("Review")


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
    rating = Column(Integer)
    pokemon_id = Column(Integer, ForeignKey("pokemon.id"))
    pokemon = relationship("Pokemon", back_populates="reviews")
    reviewer_id = Column(ForeignKey("reviewer.id", ondelete="CASCADE"))
    reviewer = relationship("Reviewer")


class Reviewer(Base):
    __tablename__ = "reviewer"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(150))
    last_name = Column(String(150))
