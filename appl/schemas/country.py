from pydantic import BaseModel


class CountryResponse(BaseModel):
    id: int
    name: str
