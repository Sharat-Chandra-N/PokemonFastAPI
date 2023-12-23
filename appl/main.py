from fastapi import FastAPI

from .controllers import category, country, pokemon

app = FastAPI(title="Pokemon Review System")

app.include_router(category.router)
app.include_router(country.router)
app.include_router(pokemon.router)


@app.get("/", tags=["Root"])
def root():
    return {"Application": "Pokemon Review System"}
