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

if command == 'start':
    if param is None:
        print('Please provide pong_time_ms as parameter for start command')
        sys.exit(1)
    pong_time_ms = int(param)
   # Create an instance of MessageHandler
    mh = MessageHandler()
    print(f'Starting pong game with {pong_time_ms}ms interval between pongs')

    try:
        mh.start_game(pong_time_ms, BackgroundTasks())
    except KeyboardInterrupt:
        print('\nGame paused')
        sys.exit(0)
    except Exception as e:
        print(f'Error: {e}')

    # while True:
    #     try:
    #         response = requests.get(instance1_url + '/ping/' + str(ping_interval))
    #         print(response.text)

    #         time.sleep(ping_interval)

    #         response = requests.get(instance2_url + '/pong/' + str(ping_interval))
    #         print(response.text)

    #         time.sleep(ping_interval)
    #     except KeyboardInterrupt:
    #         print('\nGame paused')
    #         sys.exit(0)
    #     except Exception as e:
    #         print(f'Error: {e}')

elif command == 'pause':
    print('Pausing the game')
    if pong_time_ms is not None:
        pong_time_ms = None
    print('Resuming the game')
    sys.exit(0)

elif command == 'resume':
    if pong_time_ms is None:
        print('Game not started yet. Use start command to start the game')
        sys.exit(1)
    print('Resuming the game')
    while True:
        try:
            response = requests.get(instance1_url + '/ping')
            print(response.text)
            time.sleep(ping_interval)
        except KeyboardInterrupt:
            print('\nGame paused')
            sys.exit(0)
        except Exception as e:
            print(f'Error: {e}')

elif command == 'stop':
    print('Stopping the game')
    sys.exit(0)

else:
    print('Invalid command')
    sys.exit(1)