from datetime import datetime
from typing import List

from pydantic import BaseModel


class PokemonReviewerResponse(BaseModel):
    id: int
    first_name: str
    last_name: str

    class Config:
        from_attributes = True


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
    reviewer: PokemonReviewerResponse

    class Config:
        from_attributes = True


class PokemonResponse(BaseModel):
    id: int
    name: str
    birth_date: datetime
    category: PokemonCategoryResponse
    reviews: List[PokemonReviewResponse]
