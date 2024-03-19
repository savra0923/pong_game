# instance1.py
from fastapi import FastAPI
import requests
import asyncio

app = FastAPI()

instance2_url = "http://localhost:8001"  # Change this to the URL of instance2
pong_time_ms = 1000  # Milliseconds between pings


@app.get("/")
async def ping_instance2():
    response = requests.get(instance2_url + "/ping")
    return response.text


@app.get("/pong")
async def pong():
    await asyncio.sleep(pong_time_ms / 1000)
    response = requests.get(instance2_url + "/")
    return response.text