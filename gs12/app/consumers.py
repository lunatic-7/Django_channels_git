# Topic - Generic Consumer (WebsocketConsumer and AsyncWebsocketConsumer)

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

# Websocket Consumer

class MyWebsocketConsumer(WebsocketConsumer):

    # This handler is caleed when client initially opens a connection and is about to finish the WebSocket handshake.
    def connect(self):
        print("Websocket Connected...")
        self.accept()  # To accept the connection

    # This handler is called when data received from the client
    def receive(self, text_data=None, bytes_data=None):
        print("Message received from client...", text_data)
        self.send(text_data="Salam, Wasif ji!")  # To send message from server to client
        # self.close()  # To force-close the connection
        # self.close(code=4123)  # To send a custom websocket error code

    # This handler is called when either connction to the client is lost, either from the client closing the connection, the server closing the connection or loss of tge socket.
    def disconnect(self, close_code):
        print("Websocket Disconnected...", close_code)

# AsyncWebsocket Consumer

class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):

    # This handler is caleed when client initially opens a connection and is about to finish the WebSocket handshake.
    async def connect(self):
        print("Websocket Connected...")
        await self.accept()  # To accept the connection

    # This handler is called when data received from the client
    async def receive(self, text_data=None, bytes_data=None):
        print("Message received from client...", text_data)
        await self.send(text_data="Salam, Wasif ji!")  # To send message from server to client
        # await self.close()  # To force-close the connection
        # awiat self.close(code=4123)  # To send a custom websocket error code

    # This handler is called when either connction to the client is lost, either from the client closing the connection, the server closing the connection or loss of tge socket.
    async def disconnect(self, close_code):
        print("Websocket Disconnected...", close_code)
