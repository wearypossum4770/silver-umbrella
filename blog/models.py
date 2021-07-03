from django.contrib.auth import get_user_model
from django.db.models import (
    CASCADE,
    CharField,
    DateTimeField,
    ForeignKey,
    ImageField,
    Model,
    OneToOneField,
    TextField,
)
from PIL import Image

User = get_user_model()


class Blog(Model):
    owner = OneToOneField(
        User, on_delete=CASCADE, related_name="blog_owner", null=True, blank=True
    )
    title = CharField(max_length=100, null=True, blank=True)
    content = TextField(null=True, blank=True)
    date_posted = DateTimeField(auto_now_add=True, null=True, blank=True)
    date_modified = DateTimeField(auto_now=True, null=True, blank=True)
    author = ForeignKey(
        User, on_delete=CASCADE, related_name="blog_author", null=True, blank=True
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
