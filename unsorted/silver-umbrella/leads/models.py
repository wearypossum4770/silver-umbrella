from django.db.models import (
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    DecimalField,
    FileField,
    Model,
    TextChoices,
    TextField,
)
from django.utils.translation import gettext_lazy as _


class Attachment(Model):
    date_modified = DateTimeField(auto_now=True)
    date_created = DateTimeField(auto_now_add=True)


class Lead(Model):
    """
    Allows a contact log to be created for the user type Patient
    """

    class Disposition(TextChoices):
        ABANDONED = "", _("Caller abandoned in queue")
        SCHEDULED = "SCH", _("Caller qppointment scheduled")

    company = CharField(max_length=100, null=True, blank=True)
    location = CharField(max_length=100, null=True, blank=True)
    start_date = DateField(null=True, blank=True)
    end_date = DateField(null=True, blank=True)
    application_submission = FileField(
        default="", upload_to="employment/job_applications/%Y/%m/%d/"
    )
    disposition = CharField(max_length=3, choices=Disposition.choices, null=True)
    internal_notes = TextField(null=True, blank=True)

    def __str__(self):
        return f"position: {self.role_name} company: {self.company}"

    def start_timer(self):
        ...

    def end_timer(self):
        ...


def get_object(queryset=None):
    return queryset
    # return Ticket.objects.get(uuid=self.kwargs.get("uuid"))
