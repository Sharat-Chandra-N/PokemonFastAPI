from datetime import datetime

from pydantic import BaseModel


class PokemonResponse(BaseModel):
    id: int
    name: str
    birth_date: datetime
