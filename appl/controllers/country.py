from typing import List

from fastapi import APIRouter, Depends, Form, HTTPException, status
from sqlalchemy.orm import Session

from ..database import database
from ..models import model
from ..schemas import country

router = APIRouter(prefix="/country", tags=["Country"])


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[country.CountryResponse]
)
def get_countries(db: Session = Depends(database.get_db)):
    country_list = db.query(model.Country).all()
    return country_list


@router.post(
    "/", status_code=status.HTTP_200_OK, response_model=country.CountryResponse
)
def get_country_by_id(id: int = Form(...), db: Session = Depends(database.get_db)):
    country = db.query(model.Country).filter(model.Country.id == id).first()
    if country is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Country Not Found"
        )
    return country


@router.post(
    "/owners",
    status_code=status.HTTP_200_OK,
    response_model=List[country.CountryOwnerResponse],
)
def get_owners_by_country(id: int = Form(...), db: Session = Depends(database.get_db)):
    owners = db.query(model.Owner).filter(model.Owner.country_id == id).all()
    return owners
