from typing import List

from pydantic import BaseModel


class ReviewerReviewResponse(BaseModel):
    id: int
    title: str
    text: str
    rating: int

    class Config:
        from_attributes = True


class ReviewerResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    reviews: List[ReviewerReviewResponse]
