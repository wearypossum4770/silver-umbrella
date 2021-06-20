from django.db.models import Model, TextField


class Task(Model):
    name = TextField()
