# Topic - Chat App with Database

from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json
from .models import Group, Chat


class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print("Websocket Connected...", event)
        # Get default channel layer from a project
        print("Channel Layer...", self.channel_layer)
        print("Channel Name...", self.channel_name)  # Get channel name

        self.group_name = self.scope['url_route']['kwargs']['groupkanaam']  # Prints group name sent from url
        print("Group name in server", self.group_name)

        # Add a channel to a new or existing group
        # Note : We have used async_to_sync because by default (self.channel_layer.group_add) this function is
        # async and we are using SyncConsumer here.
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,  # group name
            self.channel_name
        )
        self.send({
            'type': 'websocket.accept',
        })

    def websocket_receive(self, event):
        print("Message Received from client...", event)

        data = json.loads(event['text'])
        print("Ye message hai bro database mai save krne ke liye...", data['msg'])

        # Find group object
        group = Group.objects.get(name=self.group_name)

        # Create new chat object
        chat = Chat(
            content = data['msg'],
            group = group
        )
        chat.save()

        async_to_sync(self.channel_layer.group_send)(
            self.group_name,  # group name
            {
                'type': 'chat.message',
                'message': event['text']
            }
        )

    def chat_message(self, event):
        print('Event...', event)
        print('Actual Data...', event['message'])
        self.send({
            'type': 'websocket.send',
            'text': event['message']
        })

    def websocket_disconnect(self, event):
        print("Websocket Disconnected...", event)
        # Get default channel layer from a project
        print("Channel Layer...", self.channel_layer)
        print("Channel Name...", self.channel_name)  # Get channel name

        # Discarding a Group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,  # group name
            self.channel_name
        )
        raise StopConsumer()
