from fastapi import FastAPI, HTTPException
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


@app.get("/items/{item_id}", responses={404: {"model": NotFoundError}})
async def get_item(item_id: int):
    if item_id not in item_ids:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}
