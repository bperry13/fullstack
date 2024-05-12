from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    id: int
    name: str
    age: int

DB: List[Person] = [
    Person(id=1, name="Chewie", age=15),
    Person(id=2, name="Tootsie", age=2),
    Person(id=3, name="Lulu", age=6)
]

@app.get("/api")
def read_root():
    return DB

