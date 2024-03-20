# instance1.py
from fastapi import FastAPI, HTTPException
import requests
import asyncio
import sys
import time

app1 = FastAPI()
app2 = FastAPI()

pong_time_ms = 1000  # Milliseconds between pings
instance1_url = "http://localhost:8000"
instance2_url = "http://localhost:8001"
ping_interval = pong_time_ms / 1000

@app1.get("/ping")
async def ping():
    try:
        response = requests.post(instance2_url + "/pong")
        # print(f"Ping from instance1. Response: {response.json()['message']}")
        return {"message": f"Ping from instance1. Response: {response.json()['message']}"}
    except Exception as e:
        raise HTTPException(status_code=501, detail=f"Error pinging instance2: {e}")

@app2.get("/ping")
async def pong():
    try:
        response = requests.post(instance1_url + "/pong")
        # print(f"Ping from instance2. Response: {response.json()['message']}")
        return {"message": f"Ping from instance2. Response: {response.json()['message']}"}
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Error pinging instance1: {e}")
    
@app1.post("/pong")
async def pong():
    return {"message": "Pong from instance1"}

@app2.post("/pong")
async def ping():
    return {"message": "Pong from instance2"}
