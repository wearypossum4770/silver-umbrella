from datetime import date, timedelta

from cuid import cuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    CheckConstraint,
    DateField,
    DateTimeField,
    ImageField,
    ManyToManyField,
    Model,
    OneToOneField,
    Q,
    TextChoices,
    TextField,
)
from django.utils.translation import gettext_lazy as _

User = settings.AUTH_USER_MODEL
# Testing ideas https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing


def validate_date_of_birth(is_patient, value=None):
    if is_patient and value is None:
        raise ValidationError(
            _("%(value)s is not a valid date"),
            params={"value": value},
        )


class User(AbstractUser):
    class Prefix(TextChoices):
        MR = "Mr", _("Single or Married Man")
        MRS = "Mrs", _("Married Woman")
        MS = "Ms", _("Single or Married Woman")
        DR = "Dr", _("Medical Doctor")
        HON = "Hon", _("Honorable (Judge, Justice, other High Ranking Gov official")
        ELD = "Eld", _("Elder (religious title)")
        FTH = "Fth", _("Father (religious title)")
        BTH = "Bth", _("Brother (religious title)")
        SIS = "Sis", _("Sister (nun or other female religious leader)")
        REV = "Rev", _("Reverand (Religious leader")
        RAB = "Rab", _("Rabbi (religious leader usually of jewish faith)")
        __empty__ = _("No Selection, Declined To Answer")

    class Suffix(TextChoices):
        PHD = "PhD", _("Doctoralily Educated")
        ESQ = "Esq", _("Esquire, Lawyer")
        __empty__ = _("No Selection, Declined To Answer")

    madien_name = CharField(max_length=100, blank=True, null=True)
    nickname = CharField(max_length=100, blank=True, null=True)
    first_name = CharField(max_length=100, blank=True, null=True)
    last_name = CharField(max_length=100, blank=True, null=True)
    middle_name = CharField(max_length=20, blank=True, null=True)
    title = CharField(max_length=20, blank=True, null=True)
    honorific_prefix = CharField(
        max_length=4,
        choices=Prefix.choices,
        default=Prefix.__empty__,
        blank=True,
        null=True,
    )
    honorific_suffix = CharField(
        max_length=4,
        choices=Suffix.choices,
        default=Suffix.__empty__,
        blank=True,
        null=True,
    )
    suffix = CharField(max_length=10, blank=True, null=True)
    date_of_birth = DateField(blank=True, null=True)
    is_patient = BooleanField(default=False)
    is_clinic_staff = BooleanField(default=False)
    date_of_death = DateField(null=True, blank=True)
    retention_only = BooleanField(default=False)
    do_not_contact = BooleanField(default=False)
    # internal_notes = TextField(default="", null=True, blank=True)
    # def clean_fields(self):
    #     super().clean_fields()

    def clean(self, *args, **kwargs):
        validate_date_of_birth(self.is_patient, self.date_of_birth)
        self.handle_deceased()

        if self.first_name is not None:
            self.first_name.strip().capitalize()
        if self.middle_name is not None:
            self.middle_name.strip().capitalize()
        if self.last_name is not None:
            self.last_name.strip().capitalize()
        if self.suffix is not None:
            self.suffix.strip().capitalize()
        super().clean(*args, **kwargs)

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(date_of_death__lte=date.today() + timedelta(days=1)),
                name="not_dead_tomorrow",
            ),
            CheckConstraint(
                check=Q(date_of_birth__lte=date.today()), name="born_before_today"
            ),
        ]

    @property
    def mark_decedent_inactive(self):
        self.is_active = False

    @property
    def mark_retention_only(self):
        self.retention_only = True

    @property
    def full_name(self):
        full_name = ""
        full_name += f" {self.first_name}" if self.first_name else ""
        full_name += f" {self.middle_name}" if self.middle_name else ""
        full_name += f" {self.last_name}" if self.last_name else ""
        full_name += f" {self.suffix}" if self.suffix else ""
        return full_name

    def __str__(self):
        return f"User account: {self.full_name}"

    @property
    def require_date_of_birth(self):
        validate_date_of_birth(self.user.is_patient, self.date_of_birth)
        return "Patient has date of birth"

    def email_user(self, subject=None, body=None, cc=[], bcc=[]):

        if self.do_not_contact == True:
            send_mail(
                subject,
                body,
                None,
                [*cc, *bcc, self.email],
                fail_silently=False,
            )

        return "No Error"

    def handle_deceased(self):
        if self.date_of_death is not None and date.today() > self.date_of_death:
            self.mark_retention_only
            self.mark_decedent_inactive
            return "Cmpl"


class Address(Model):
    class Type(TextChoices):
        MAIL = "MAIL", _("Mailing")
        RESIDENTIAL = "RESD", _("Residential")
        BUSINESS = "BUSN", _("Business")

    idempotent_key = CharField(max_length=50, default=cuid)
    address_type = CharField(max_length=4, choices=Type.choices)
    street1 = CharField(max_length=100)
    street2 = CharField(max_length=100, null=True, blank=True)
    state = CharField(max_length=4)
    city = CharField(max_length=50)
    zipcode = CharField(max_length=10)

    def __str__(self):
        return f" {self.street1}  {self.city},  {self.state}  {self.zipcode}"


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    image = ImageField(upload_to="raw_profile_pictures", default="default.webp")
    addresses = ManyToManyField(Address, blank=True)
    mobile_number = CharField(
        max_length=15,
        null=True,
        blank=True,
        help_text="Numbers only no spaces or characters. Example: xxxxxxxxxx",
    )
    internal_notes = TextField(default="", null=True, blank=True)

    def __str__(self):
        return f" {self.user.full_name}"
