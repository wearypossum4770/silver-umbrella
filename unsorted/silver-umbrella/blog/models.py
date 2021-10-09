from django.contrib.auth import get_user_model
from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    ForeignKey,
    ImageField,
    Model,
    OneToOneField,
    TextChoices,
    TextField,
)
from django.utils.translation import gettext_lazy as _
from PIL import Image

User = get_user_model()

# https://bleachmanga.biz/read-bleach-chapter-526-the-battle-updated/
class Post(Model):
    class Type(TextChoices):
        # https://www.abbreviations.com/serp.php?st=ANNOUNCEMENT&qtype=2
        ANNOUNCEMENT = "ANNCMNT", _("Public Announcement")
        CONCEALMENT = "CONCMNT", _("Private Post")

    owner = OneToOneField(
        User, on_delete=CASCADE, related_name="blog_owner", null=True, blank=True
    )
    is_public = BooleanField(default=False)
    publication_type = CharField(
        max_length=7, choices=Type.choices, default=Type.CONCEALMENT
    )
    title = CharField(max_length=100, null=True, blank=True)
    content = TextField(null=True, blank=True)
    date_posted = DateTimeField(auto_now_add=True, null=True, blank=True)
    date_modified = DateTimeField(auto_now=True, null=True, blank=True)
    date_expired = DateField(null=True, blank=True)
    author = ForeignKey(
        User, on_delete=CASCADE, related_name="blog_author", null=True, blank=True
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
