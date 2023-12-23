from datetime import datetime

from pydantic import BaseModel


class PokemonCategoryResponse(BaseModel):
    id: int
    name: str


class PokemonResponse(BaseModel):
    id: int
    name: str
    birth_date: datetime
    category: PokemonCategoryResponse
