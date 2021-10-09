from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.models import (
    CASCADE,
    CharField,
    DateTimeField,
    ForeignKey,
    ManyToManyField,
    Model,
    OneToOneField,
    TextField,
)
from django.utils import timezone

User = get_user_model()


class Contact(Model):
    user = ForeignKey(User, related_name="friends", on_delete=CASCADE)
    friends = ManyToManyField("self", blank=True)

    def __str__(self):
        return self.user.username


class Message(Model):
    # title=CharField(max_length=50, null=True, blank=True)
    author = ForeignKey(User, related_name="messages", on_delete=CASCADE)
    content = TextField()
    timestamp = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} sent: {self.content}"

    def last_10_messages(self):
        return Message.objects.order_by("-timestamp").all()[:10]


class Chat(Model):
    participants = ManyToManyField(Contact, blank=True)
    messages = ManyToManyField(Message, blank=True)

    def __str__(self):
        return f"{self.pk}"
