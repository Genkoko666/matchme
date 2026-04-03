from fastapi import FastAPI
import redis
import os



app = FastAPI()
@app.get("/")
async def root():
    return {"message": "FastAPI working"}
