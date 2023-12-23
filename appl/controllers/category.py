from typing import List

from fastapi import APIRouter, Depends, Form, HTTPException, status
from sqlalchemy.orm import Session

from ..database import database
from ..models import model
from ..schemas import category

router = APIRouter(prefix="/category", tags=["Category"])


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[category.CategoryResponse]
)
def get_categories(db: Session = Depends(database.get_db)):
    category_list = db.query(model.Category).all()
    return category_list


@router.post(
    "/", status_code=status.HTTP_200_OK, response_model=category.CategoryResponse
)
def get_category_by_id(id: int = Form(...), db: Session = Depends(database.get_db)):
    category = db.query(model.Category).filter(model.Category.id == id).first()
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category Not Found"
        )
    return category


@router.post("/pokemon", status_code=status.HTTP_200_OK)
def get_pokemons_by_category(
    id: int = Form(...), db: Session = Depends(database.get_db)
):
    return {"status": id}
