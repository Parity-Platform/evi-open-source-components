from typing import Union
from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"service": "EVI Verifier proxy"}


@app.post("/verify")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}