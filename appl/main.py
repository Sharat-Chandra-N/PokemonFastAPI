from fastapi import FastAPI

from .database import database
from .models import model

app = FastAPI(title="Pokemon Review System")

# model.Base.metadata.create_all(bind=database.engine)


@app.get("/", tags=["Root"])
def root():
    return {"Application": "Pokemon Review System"}
