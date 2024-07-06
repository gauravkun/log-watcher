import asyncio
import websockets
import os

LOG_FILE_PATH = os.path.join("/", "Users", "gauravsarangi", "Downloads", "log-watcher", "logfile.log")

async def tail_f(websocket, path): 
    with open(LOG_FILE_PATH, 'rb') as file:

        lines = file.readlines()[-10:]
        await websocket.send(''.join(line.decode('utf-8') + '\n' for line in lines))

        while True:
            where = file.tell()
            line = file.readline()
            if not line:
                await asyncio.sleep(1)
                file.seek(where)
            else:
                await websocket.send(line.decode('utf-8') + '\n')

start_server = websockets.serve(tail_f, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

