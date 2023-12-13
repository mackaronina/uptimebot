from telethon.sync import TelegramClient
import time
from flask import Flask
import asyncio

api_id = 20319557
api_hash = '1eb6e800411c9c7cbe90d39db9b7d1c3'

app = Flask(__name__)
@app.route('/')
def get_ok():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    with TelegramClient('session_name', api_id, api_hash, loop=loop) as client:
        #client = TelegramClient('session_name', api_id, api_hash, loop=loop)
        client.start()
        m = client.send_message(-1001694727085, 'Hello! Talking to you from Telethon')
        time.sleep(0.1)
        client.delete_messages(entity = -1001694727085, message_ids = [m.id])
        return 'ok', 200
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)

