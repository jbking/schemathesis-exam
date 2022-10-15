import random

from fastapi import Body, FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


item_ids = [1, 2, 3, 5, 7, 11]


class NotFoundError(BaseModel):
    detail: str

    class Config:
        schema_extra = {
            "example": {"detail": "string"}
        }


@app.get("/items/")
async def get_items():
    return {"items": [{"item_id": item_id} for item_id in item_ids]} 


@app.post("/items/", status_code=201)
async def create_item(name: str = Body()):
    item_id = random.randint(0, 10000)
    while item_id in item_ids:
        item_id = random.randint(0, 10000)
    item_ids.append(item_id)
    return {"item_id": item_id}


@app.get("/items/{item_id}", responses={404: {"model": NotFoundError}})
async def get_item(item_id: int):
    if item_id not in item_ids:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}
