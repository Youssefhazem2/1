from typing import Union

from fastapi import FastAPI

app = FastAPI()

students ={
    1:{
        "name":"john",
        "age":17,
        "class":"year 12"
    }
}

@app.get("/")
def index():
    return {"name":"First Data"}
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
