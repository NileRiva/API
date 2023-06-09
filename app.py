# app.py
import uvicorn
from fastapi import FastAPI
from fastapi import FastAPI,HTTPException,Request
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from timeit import default_timer as timer
import csv

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/test")
async def test(request:Request):
    #receive a json object
    file = open('data.csv', 'a', newline='')
    writer = csv.writer(file)
    start = timer()
    test = await request.json()
    end = timer()
    writer.writerow([end-start])
    print(end - start)

if __name__ == "__main__":
    uvicorn.run("app:app")