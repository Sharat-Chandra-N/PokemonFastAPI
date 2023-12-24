from datetime import datetime

from pydantic import BaseModel


class OwnerPokemonResponse(BaseModel):
    name: str
    birth_date: datetime


class OwnerResponse(BaseModel):
    id: int
    gym: str
    first_name: str
    last_name: str
