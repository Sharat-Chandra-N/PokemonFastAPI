from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from ..database.database import Base


class Pokemon(Base):
    __tablename__ = "pokemon"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150))
