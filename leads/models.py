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
    class Status(TextChoices):
        APPLIED = "APP", _("Applied for position")
        INTERVIEWED = "INT", _("Interview with organization")
        ACCPETED = "ACT", _("Offer Extended, Accepted")
        DECLINED = "DCL", _("Offer Extended, Voluntarily withdrawl")
        WITHDRAW = "WDW", _("Voluntary Candidancy Withdrawl")
        DENIED = "DNY", _("Involuntary Candidancy Withdrawl")

    class Employment(TextChoices):
        FULL_TIME = "FT", _("Full-time Position")
        PART_TIME = "PT", _("Part-time Position")
        CONTRACT = "CT", _("Contract Position")
        TEMPORARY = "TP", _("Temporary Position")
        SEASONAL = "SN", _("Seasonal Position")
        INTERNSHIP = "IN", _("Internship Position")
        APPRENTICESHIP = "AP", _("Apprenticeship Position")

    company = CharField(max_length=100, null=True, blank=True)
    location = CharField(max_length=100, null=True, blank=True)
    base_salary = DecimalField(null=True, blank=True, max_digits=9, decimal_places=2)
    min_salary = DecimalField(null=True, blank=True, max_digits=9, decimal_places=2)
    max_salary = DecimalField(null=True, blank=True, max_digits=9, decimal_places=2)
    role_name = CharField(max_length=100, null=True, blank=True)
    remote_position = BooleanField(default=True)
    start_date = DateField(null=True, blank=True)
    end_date = DateField(null=True, blank=True)
    employment_type = CharField(
        max_length=2, choices=Employment.choices, default=Employment.FULL_TIME
    )
    employer_overview = TextField(null=True, blank=True)
    experience_requirements = CharField(max_length=100, null=True, blank=True)
    experience_preferred = CharField(max_length=100, null=True, blank=True)
    application_submission = FileField(
        default="", upload_to="employment/job_applications/%Y/%m/%d/"
    )
    application_status = CharField(
        max_length=3, choices=Status.choices, default=Status.APPLIED
    )
    notes = TextField(null=True, blank=True)

    def __str__(self):
        return f"position: {self.role_name} company: {self.company}"


def get_object(queryset=None):
    return queryset
    # return Ticket.objects.get(uuid=self.kwargs.get("uuid"))
