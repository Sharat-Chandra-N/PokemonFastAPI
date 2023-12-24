from pydantic import BaseModel


class ReviewResponse(BaseModel):
    id: int
    title: str
    text: str
    rating: int
