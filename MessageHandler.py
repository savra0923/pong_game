from fastapi import HTTPException, FastAPI, BackgroundTasks
import requests
import threading
import time
import logging


class MessageHandler:
    def __init__(self):
        self.instance1_url = "http://localhost:8000"
        self.instance2_url = "http://localhost:8001"
        self.ping_interval = 0
        self.run_game = False
        self.app = FastAPI()

    def send_ping_from_instance1(self):
        logging.info("Background task started")
        try:
            response = requests.get(f"{self.instance1_url}/ping")
            print(response.json())
            logging.info("Background task completed")
            return response.json()
        except Exception as e:
            raise HTTPException(status_code=501, detail=f"Error sending ping from instance1: {e}")

    def send_ping_from_instance2(self):
        logging.info("Background task started")
        try:
            response = requests.get(f"{self.instance2_url}/ping")
            print(response.json())
            logging.info("Background task completed")
            return response.json()
        except Exception as e:
            raise HTTPException(status_code=502, detail=f"Error sending ping from instance2: {e}")

    def start_game(self, pong_time_ms: float, background_tasks: BackgroundTasks):
        @self.app.get("/")
        async def ping():
            self.ping_interval = pong_time_ms / 1000
            self.run_game = True
            
            # while self.run_game:
            #     background_tasks.add_task(self.send_ping_from_instance1, self.instance1_url)
            #     time.sleep(self.ping_interval)
            #     background_tasks.add_task(self.send_ping_from_instance2, self.instance2_url)
            #     time.sleep(self.ping_interval)

            while self.run_game:

                # Send ping from instance 1
                response_instance1 = self.send_ping_from_instance1()
                # print(response_instance1)
                time.sleep(self.ping_interval)

                # Send ping from instance 2
                response_instance2 = self.send_ping_from_instance2()
                # print(response_instance2)
                time.sleep(self.ping_interval)
            
    def pause_game(self):
        self.run_game = False
    
    def resume_game(self):
        self.run_game = True