from datetime import datetime

from pydantic import BaseModel


class PokemonCategotyRespone(BaseModel):
    name: str
    birth_date: datetime


class CategoryResponse(BaseModel):
    id: int
    name: str
