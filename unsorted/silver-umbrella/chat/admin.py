from django.contrib import admin

from chat.models import Chat, Contact, Message

admin.site.register(Chat)
admin.site.register(Contact)
admin.site.register(Message)
