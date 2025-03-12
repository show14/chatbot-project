import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: int


@app.get("/items/{item_name}")
def get_item(item_name):
    return {"name": item_name, "price": 200}


@app.post("/items/new")
def add_item(item: Item):
    return item


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
