from telethon.sync import TelegramClient
import time
from flask import Flask
import asyncio

api_id = 17453825
api_hash = 'aa6df76596b13eb999078e2e9796ff95'

app = Flask(__name__)
@app.route('/')
def get_ok():
    with TelegramClient('session_name', api_id, api_hash, loop=loop) as client:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        #client = TelegramClient('session_name', api_id, api_hash, loop=loop)
        client.start()
        m = client.send_message(-1001694727085, 'Hello! Talking to you from Telethon')
        time.sleep(2)
        client.delete_messages(entity = -1001694727085, message_ids = [m.id])
        return 'ok', 200
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)

