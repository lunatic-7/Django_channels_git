# Topic - More on Consumers and Routing

from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer


class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print("Websocket connected...", event)
        self.send({
            'type': 'websocket.accept',
        })

    def websocket_receive(self, event):
        print("Message received from client", event)
        print(event['text'])
        self.send({
            'type': 'websocket.send',
            'text': "Message from Application hai ullu!",
        })

    def websocket_disconnect(self, event):
        print("Websocket disconnected...", event)
        raise StopConsumer()