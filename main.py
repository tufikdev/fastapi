from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World New !"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/items/")
def read_item_all(q: Optional[str] = None):
    return {"items": [{"item_id","item01"},{"item_id","item02"},{"item_id","item03"}], "q": q}
