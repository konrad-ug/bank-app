from typing import Union
from Konto import Konto
from fastapi import FastAPI, Request, Body
from pydantic import BaseModel
app = FastAPI()

app.request_count = 0

@app.get("/")
def read_root():
    app.request_count = app.request_count + 1
    return {"Hello": f"World {app.request_count}"}

class Item(BaseModel):
    name: str
    nip: str

@app.post("/zaloz_konto")
def zaloz_konto(request: Body):
    print(request.json())
    # konto = Konto(Item.name, "ffff", Item.nip)
    return {"Hello": f"World {request.json()}"}