from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

User = get_user_model()


def index(request):
    return render(request, "chat/index.html")


@database_sync_to_async
@login_required
def room(request, room_name):
    return render(
        request,
        "chat/room.html",
        {
            "room_name": room_name,
            "userId": request.user.id,
            "username": request.user.username,
        },
    )


@database_sync_to_async
def get_last_10_messages(chatId):
    chat = get_object_or_404(Chat, id=chatId)
    return chat.messages.order_by("-timestamp").all()[:10]


@database_sync_to_async
def get_user_contact(username):
    user = get_object_or_404(User, username=username)
    return get_object_or_404(Contact, user=user)


@database_sync_to_async
def get_current_chat(chatId):
    return get_object_or_404(Chat, id=chatId)
