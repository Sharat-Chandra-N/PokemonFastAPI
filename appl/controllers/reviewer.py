from typing import List

from fastapi import APIRouter, Depends, Form, HTTPException, status
from sqlalchemy.orm import Session

from ..database import database
from ..models import model
from ..schemas import reviewer

router = APIRouter(prefix="/reviewer", tags=["Reviewer"])


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[reviewer.ReviewerResponse]
)
def get_reviewers(db: Session = Depends(database.get_db)):
    reviewers_list = db.query(model.Reviewer).all()
    return reviewers_list


@router.post(
    "/", status_code=status.HTTP_200_OK, response_model=reviewer.ReviewerResponse
)
def get_reviewers_by_id(id: int = Form(...), db: Session = Depends(database.get_db)):
    reviewer = db.query(model.Reviewer).filter(model.Reviewer.id == id).first()
    return reviewer
