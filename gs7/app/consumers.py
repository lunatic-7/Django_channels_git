# Topic - Real time data with Frontend

from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio  # need to use in sleep of Async type
import json

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print("Websocket connected...", event)
        self.send({
            'type': 'websocket.accept',
        })

    def websocket_receive(self, event):
        print("Message received from client...", event['text'])
        for _ in range(8):
            self.send({
                'type': 'websocket.send',
                'text': json.dumps({"count": _}),
            })
            sleep(1)  # Give rest for 1 second so that we can see the data coming...

    def websocket_disconnect(self, event):
        print("Websocket disconnected...", event)
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("Websocket connected...", event)
        await self.send({
            'type': 'websocket.accept',
        })

    async def websocket_receive(self, event):
        print("Message received from client", event)
        print(event['text'])
        for _ in range(8):
            await self.send({
                'type': 'websocket.send',
                'text': f"Message from Application hai ullu {_}!",
            })
            await asyncio.sleep(1)  # Give rest for 1 second so that we can see the data coming...

    async def websocket_disconnect(self, event):
        print("Websocket disconnected...", event)
        raise StopConsumer()
