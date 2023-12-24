from typing import List

from fastapi import APIRouter, Depends, Form, HTTPException, status
from sqlalchemy.orm import Session

from ..database import database
from ..models import model
from ..schemas import pokemon

router = APIRouter(prefix="/pokemon", tags=["Pokemon"])


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[pokemon.PokemonResponse]
)
def get_pokemon(db: Session = Depends(database.get_db)):
    pokemon_list = db.query(model.Pokemon).all()
    return pokemon_list


@router.post(
    "/", status_code=status.HTTP_200_OK, response_model=pokemon.PokemonResponse
)
def get_pokemon_by_id(id: int = Form(...), db: Session = Depends(database.get_db)):
    pokemon = db.query(model.Pokemon).filter(model.Pokemon.id == id).first()
    if pokemon is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon Not Found"
        )
    return pokemon


@router.post("/rating", status_code=status.HTTP_200_OK)
def get_ratings_of_pokemon_by_id(
    id: int = Form(...), db: Session = Depends(database.get_db)
):
    pokemon_list = db.query(model.Review).filter(model.Review.pokemon_id == id).all()
    if pokemon_list:
        sumoflist = 0
        for x in pokemon_list:
            sumoflist = x.rating + sumoflist
        return {"rating": round(sumoflist / len(pokemon_list), 2)}
    return pokemon_list
