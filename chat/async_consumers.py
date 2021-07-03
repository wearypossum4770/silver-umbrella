import json
from random import randint

from asgiref.sync import async_to_sync, sync_to_async
from channels.auth import login
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model

from chat.models import Chat, Contact, Message
from chat.views import get_last_10_messages

User = get_user_model()


def easter_eggs(message):
    return {}.get(message)


class ChatConsumer(AsyncWebsocketConsumer):
    # commands = {
    #     "fetch_messages": fetch_messages,
    #     "new_message": new_message,
    # }
    # channel_layer_alias = "async_chat_object"
    @database_sync_to_async
    def get_name(self):
        return User.objects.all()[0].name

    async def connect(self):
        self.room_name = self.scope.get("url_route").get("kwargs").get("room_name")
        self.room_group_name = f"chat_{self.room_name}"
        print(self.scope.get("user"))
        # Join room group
        print(self.get_name())
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):

        text_data_json = json.loads(text_data)
        print(text_data_json)
        message = text_data_json.get("message")
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "username": self.scope.get("user").username,
                "message": message,
            },
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
