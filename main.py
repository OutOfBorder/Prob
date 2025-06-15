from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    a: float
    b: float

@app.post("/add")
def add_numbers(numbers: Numbers):
    result = numbers.a + numbers.b
    return {"c": result}






