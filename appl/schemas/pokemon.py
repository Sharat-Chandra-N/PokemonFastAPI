from datetime import datetime
from typing import List

from pydantic import BaseModel


class PokemonCategoryResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class PokemonReviewResponse(BaseModel):
    id: int
    title: str
    text: str
    rating: int

    class Config:
        from_attributes = True


class PokemonResponse(BaseModel):
    id: int
    name: str
    birth_date: datetime
    category: PokemonCategoryResponse
    reviews: List[PokemonReviewResponse]
