# Topic - Routing

from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print("Websocket connected...", event)
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print("Message received...", event)
        print("Message is ", event["text"])

    def websocket_disconnect(self, event):
        print("Websocket disconnected...", event)
        raise StopConsumer()

class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("Websocket connected...", event)
        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):
        print("Message received...", event)

    async def websocket_disconnect(self, event):
        print("Websocket disconnected...", event)
        raise StopConsumer()
