from django.db.models import CharField, Model


class Question(Model):
    question_text = CharField(max_length=100)
