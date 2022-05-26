import json
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
import uvicorn
from utils import *

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("rides.json") as f:
    data = json.load(f)


@app.get("/rides")
async def root():
    return data


@app.get("/ride/charge")
async def price(id: int):
    return charge(data[id - 1])


@app.get("/ride/duration")
async def period(id: int):
    return {
        "duration": duration(data[id - 1]["duration"]),
        "end": end_time(data[id - 1]),
    }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
