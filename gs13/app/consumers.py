# Topic - Generic Consumer (WebsocketConsumer and AsyncWebsocketConsumer)

from channels.generic.websocket import JsonWebsocketConsumer, AsyncJsonWebsocketConsumer

# Websocket Consumer

class MyJsonWebsocketConsumer(JsonWebsocketConsumer):

    # This handler is caleed when client initially opens a connection and is about to finish the WebSocket handshake.
    def connect(self):
        print("Websocket Connected...")
        self.accept()  # To accept the connection

    # This handler is called when data received from the client with decoded JSON content
    def receive_json(self, content, **kwargs):
        print("Message received from client...", content)

        # Encode the data in JSON and send it to client
        self.send_json({'message': 'Salam, Wasif ji!'})  # To send message from server to client
        # self.close()  # To force-close the connection
        # self.close(code=4123)  # To send a custom websocket error code

    # This handler is called when either connction to the client is lost, either from the client closing the connection, the server closing the connection or loss of tge socket.
    def disconnect(self, close_code):
        print("Websocket Disconnected...", close_code)

# AsyncWebsocket Consumer

class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):

    # This handler is caleed when client initially opens a connection and is about to finish the WebSocket handshake.
    async def connect(self):
        print("Websocket Connected...")
        await self.accept()  # To accept the connection

    # This handler is called when data received from the client
    async def receive_json(self, content, **kwargs):
        print("Message received from client...", content)

        # Encode the data in JSON and send it to client
        await self.send_json({'message': 'Salam, Wasif ji!'})  # To send message from server to client
        # await self.close()  # To force-close the connection
        # awiat self.close(code=4123)  # To send a custom websocket error code

    # This handler is called when either connction to the client is lost, either from the client closing the connection, the server closing the connection or loss of tge socket.
    async def disconnect(self, close_code):
        print("Websocket Disconnected...", close_code)
