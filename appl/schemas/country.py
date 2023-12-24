from pydantic import BaseModel


class CountryOwnerResponse(BaseModel):
    id: int
    gym: str
    first_name: str
    last_name: str


class CountryResponse(BaseModel):
    id: int
    name: str
