from fastapi import FastAPI, HTTPException

app = FastAPI()


item_ids = [1, 2, 3, 5, 7, 11]

@app.get("/items/")
async def get_items():
    return {"items": [{"item_id": item_id} for item_id in item_ids]} 

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id not in item_ids:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}
