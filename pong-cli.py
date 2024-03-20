# pong-cli.py
import sys
import time
import requests
from MessageHandler import MessageHandler
from fastapi import HTTPException, FastAPI, BackgroundTasks

command = sys.argv[1]
param = sys.argv[2] if len(sys.argv) > 2 else None

instance1_url = 'http://localhost:8000'
instance2_url = "http://localhost:8001"
pong_time_ms = None
ping_interval = None

mh = MessageHandler()

if command == 'start':
    if param is None:
        print('Please provide pong_time_ms as parameter for start command')
        sys.exit(1)
    pong_time_ms = int(param)
   # Create an instance of MessageHandler
    print(f'Starting pong game with {pong_time_ms}ms interval between pongs')

    try:
        mh.start_game(pong_time_ms, BackgroundTasks())
    except KeyboardInterrupt:
        print('\nGame paused')
        sys.exit(0)
    except Exception as e:
        print(f'Error: {e}')

elif command == 'pause': # sends a message to pause the game. self.run_game = False
    print('Pausing the game')
    mh.pause_game()

elif command == 'resume': # sends a message to pause the game. self.run_game = True
    mh.resume_game()

elif command == 'stop': 
    print('Stopping the game')
    sys.exit(0)

else:
    print('Invalid command')
    sys.exit(1)