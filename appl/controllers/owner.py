from typing import List

from fastapi import APIRouter, Depends, Form, HTTPException, status
from sqlalchemy.orm import Session

from ..database import database
from ..models import model
from ..schemas import owner

router = APIRouter(prefix="/owner", tags=["Owner"])


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[owner.OwnerResponse]
)
def get_owners(db: Session = Depends(database.get_db)):
    owner_list = db.query(model.Owner).all()
    return owner_list


@router.post("/", status_code=status.HTTP_200_OK, response_model=owner.OwnerResponse)
def get_owner_by_id(id: int = Form(...), db: Session = Depends(database.get_db)):
    owner = db.query(model.Owner).filter(model.Owner.id == id).first()
    if owner is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Owner Not Found"
        )
    return owner


@router.post(
    "/pokemon",
    status_code=status.HTTP_200_OK,
    response_model=List[owner.OwnerPokemonResponse],
)
def get_owners_by_country(id: int = Form(...), db: Session = Depends(database.get_db)):
    owners = db.query(model.Pokemon).filter(model.Pokemon.owner_id == id).all()
    return owners
