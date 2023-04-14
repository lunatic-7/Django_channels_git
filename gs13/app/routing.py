from django.urls import path
from .consumers import MyJsonWebsocketConsumer, MyAsyncJsonWebsocketConsumer

websocket_urlpatterns = [
    path("ws/jwsc/", MyJsonWebsocketConsumer.as_asgi()),
    path("ws/jawsc/", MyAsyncJsonWebsocketConsumer.as_asgi()),
]