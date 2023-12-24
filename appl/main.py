from fastapi import FastAPI

from .controllers import category, country, owner, pokemon, review, reviewer

app = FastAPI(title="Pokemon Review System")

app.include_router(category.router)
app.include_router(country.router)
app.include_router(pokemon.router)
app.include_router(owner.router)
app.include_router(review.router)
app.include_router(reviewer.router)


@app.get("/", tags=["Root"])
def root():
    return {"Application": "Pokemon Review System"}
