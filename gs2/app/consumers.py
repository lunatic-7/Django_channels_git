# Topic - Consumers

from channels.consumer import SyncConsumer, AsyncConsumer

# SyncConsumer

class MySyncConsumer(SyncConsumer):
    # This handler is caleed when client initially opens a connection and is about to finish the WebSocket handshake.
    def websocket_connect(self, event):
        print("Websocket Connected...")

    # This handler is called when data received from the client
    def websocket_receive(self, event):
        print("Message Received...")

    # This handler is called when either connction to the client is lost, either from the client closing the connction, the server closing the connection or loss of tge socket.
    def websocket_disconnect(self, event):
        print("Websocket Disconnected...")

# AsyncConsumer

class MyAsyncConsumer(AsyncConsumer):
    # This handler is caleed when client initially opens a connection and is about to finish the WebSocket handshake.
    async def websocket_connect(self, event):
        print("Websocket Connected...")

    # This handler is called when data received from the client
    async def websocket_receive(self, event):
        print("Message Received...")

    # This handler is called when either connction to the client is lost, either from the client closing the connction, the server closing the connection or loss of tge socket.
    async def websocket_disconnect(self, event):
        print("Websocket Disconnected...")
