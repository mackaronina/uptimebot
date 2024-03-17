from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import time
from flask import Flask
import asyncio
import g4f
import time

g4f.debug.logging = True
g4f.debug.check_version = False

api_id = 20319557
api_hash = '1eb6e800411c9c7cbe90d39db9b7d1c3'
ses = '1ApWapzMBuxJOWsDEOYd5YP32giPOOA8JbSnsGKWQ4tul4TUPE1uT2FbXqFHsXu5ImQz7RIYZvZwYqlt9hLCqpVORCTNsQVCuFIkQpZ-XoK7WSOaZYSCt_uZUkvOkHvFD6FRT5z0Wa0Eerq47yqHW9DwMw0DvJNWWLX8JB6d-ItfMShEVLvFtHdOONF6rRgH5mGP5Za7irkJp-yO9O84p4mieIS1GrMnGVfurHtI1FWELg36Vh6BazxEkx2urBgO9T1hrrNSLl_3AjD0vX8HuW6DhjQMk5nf5iyT0pcqZdi6URyeWWlxDKcuGis4io3evBIiJEBfsZHnwW7KwGQQqOGxyzDtJpd8='

app = Flask(__name__)

def generate_text():
    response = None
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-4",
            provider=g4f.Provider.ChatgptAi,
            messages=[{'role':'user','content':'Некославия это страна, граждан которой называют некославы, а мудрого правителя некокинг, её девиз это "Славься Некославия!". Некославия развитая страна которая колонизировала Марс. Также ученым удалось скрестить кошек с людьми и получить некодевочек и некомальчиков, которых очень любят некославы. Самый популярный энергетик в Некославии это "розовый монстр". Вместо машин в Некославии используют некомобили. Напиши короткое необычное пожелание доброго утра для граждан этой страны'}]
        )
    except:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            provider=g4f.Provider.FlowGpt,
            messages=[{'role':'user','content':'Некославия это страна, граждан которой называют некославы, а мудрого правителя некокинг, её девиз это "Славься Некославия!". Некославия развитая страна которая колонизировала Марс. Также ученым удалось скрестить кошек с людьми и получить некодевочек и некомальчиков, которых очень любят некославы. Самый популярный энергетик в Некославии это "розовый монстр". Вместо машин в Некославии используют некомобили. Напиши короткое необычное пожелание доброго утра для граждан этой страны'}]
        )
    print(response)
    if len(response) > 500:
        time.sleep(2)
        response = generate_text() 
    return response

@app.route('/')
def get_ok():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    with TelegramClient(StringSession(ses), api_id, api_hash, loop=loop) as client:
        client.start()
        m = client.send_message(-1001694727085, 'Hello! Talking to you from Telethon')
        time.sleep(0.1)
        client.delete_messages(entity=-1001694727085, message_ids=[m.id])
    return 'ok', 200

@app.route('/morning')
def get_morning():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    with TelegramClient(StringSession(ses), api_id, api_hash, loop=loop) as client:
        client.start()
        #text = generate_text()
        m = client.send_message(5526375200, 'Проверка')
        time.sleep(5)
        m = client.get_messages(5526375200, ids=m.id+1)
        client.forward_messages(6964908043, m)
    return 'ok', 200

@app.route('/getposts')
def get_getposts():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    with TelegramClient(StringSession(ses), api_id, api_hash, loop=loop) as client:
        client.start()
        for msg in client.get_messages('@animewebmtg', limit=3):
            if '#NecoArc' in msg.text:
                client.forward_messages('@NekocringeBot', msg)
    return 'ok', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)