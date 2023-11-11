from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_main():
    return {"message":"Hello World"}


@app.get("/items/{item_id}")
async def read(item_id : int):
    return {"id":item_id, "name": "Item One", "description":"This is item one"}