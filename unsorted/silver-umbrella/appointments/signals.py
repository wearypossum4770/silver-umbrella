from uuid import uuid4

from cuid import cuid
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from appointments.models import Appointment

# @receiver(pre_delete, sender=Appointment)
# def soft_deleted(sender, instance, *args, **kwargs):


@receiver(post_save, sender=Appointment)
def create_external_identifier(sender, instance, created, *args, **kwargs):
    if created and instance.external_identifier is None:
        instance.external_identifier = f"{uuid4()}_{cuid()}"
        instance.save()
