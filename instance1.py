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

@app1.get("/")
async def ping_instance():
    try:
        response = requests.get(instance2_url + "/ping")
        return response.text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error pinging instance2: {e}")


@app1.get("/ping")
async def ping():
    print(f"recieved PING")
    try:
        response = requests.get(instance2_url + "/pong")
        return response.text
    except Exception as e:
        raise HTTPException(status_code=501, detail=f"Error pinging instance2: {e}")


@app2.get("/pong")
async def pong():
    print(f"recieved PONG")
    try:
        await asyncio.sleep(pong_time_ms / 1000)
        response = requests.get(instance1_url + "/ping")
        return response.text
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Error pinging instance1: {e}")
