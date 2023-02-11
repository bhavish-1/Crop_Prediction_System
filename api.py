from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class EnvironmentalData(BaseModel):
    n: int
    p: int
    k: int
    temperature: int
    humidity: int
    ph: int
    rainfall: int

@app.post("/")
async def index(item: EnvironmentalData):
    return item