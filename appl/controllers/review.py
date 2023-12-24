from typing import List

from fastapi import APIRouter, Depends, Form, HTTPException, status
from sqlalchemy.orm import Session

from ..database import database
from ..models import model
from ..schemas import review

router = APIRouter(prefix="/review", tags=["Review"])


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[review.ReviewResponse]
)
def get_reviews(db: Session = Depends(database.get_db)):
    reviews_list = db.query(model.Review).all()
    return reviews_list


@router.post("/", status_code=status.HTTP_200_OK, response_model=review.ReviewResponse)
def get_review_by_id(id: int = Form(...), db: Session = Depends(database.get_db)):
    review = db.query(model.Review).filter(model.Review.id == id).first()
    if review is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Review Not Found"
        )
    return review


@router.post(
    "/pokemon",
    status_code=status.HTTP_200_OK,
    response_model=List[review.ReviewResponse],
)
def get_reviews_by_pokemon_id(
    id: int = Form(...), db: Session = Depends(database.get_db)
):
    review = db.query(model.Review).filter(model.Review.pokemon_id == id).all()
    return review
