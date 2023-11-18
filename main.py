from fastapi import FastAPI
from user_service import user_service

app = FastAPI()

@app.get("/")
async def read_main():
    return {"message":"Hello World"}


@app.get("/items/{item_id}")
async def read(item_id : int):
    return {"id":item_id, "name": "Item One", "description":"This is item one"}

@app.get("/users")
async def get_users():
    users = user_service.get_users_from_db()
    return users