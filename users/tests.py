import json
from datetime import date

import pytest
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.views import LoginView
from django.core import mail
from django.test import TestCase
from django.urls import reverse

from users.forms import UserRegisterForm
from users.models import Address, Profile

# /https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp
# file:///C:/Users/BidDaddy/Downloads/OWASP%20Application%20Security%20Verification%20Standard%204.0.2-en.pdf


def genryusai_shigekuni_yamamoto_data():
    with open(f"{settings.BASE_DIR}/users/fixtures/new_registrant.json") as _d:
        __data__ = json.load(_d)
    return __data__


email = {"subject": "Test Message", "body": "This is a new Message"}
raw_password = "🚫😎💡PASSword123!@#"
hashed = "pbkdf2_sha256$260000$D1SAgiii3dwy8YyKMsnKFA$22c8aUvcUGW+8z7TWCq8VFWCYfsJg6Pv0y1AJqj6aHU="

User = get_user_model()


@pytest.mark.asyncio
@pytest.mark.django_db
def test_user_registered():
    form = UserRegisterForm(genryusai_shigekuni_yamamoto_data())
    is_valid = form.is_valid()
    form.save()
    assert is_valid == True
    new_registrant = User.objects.get(username="genryusai.shigekuni.yamamoto")
    assert new_registrant is not None
    assert form.instance.username == "genryusai.shigekuni.yamamoto"


class TestProfile(TestCase):
    fixtures = ("datainit.json",)
    pytestmark = pytest.mark.django_db

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.staff_user = User.objects.get(pk=46)
        cls.trump = User.objects.get(pk=45)
        cls.reagan = User.objects.get(last_name="Reagan")
        cls.clinton = User.objects.get(pk=42)
        cls.profile = Profile.objects.get(user=cls.staff_user)
        cls.address = Address.objects.get(idempotent_key="ckpfzqd7l0000nbve3vq1hfgl")
        cls.trump.set_password(raw_password)
        cls.trump.save()
        cls.reagan.handle_deceased()
        cls.staff_user.handle_deceased()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_send_email_to_user(self):
        assert self.staff_user.email_user(**email) == "No Error"

    def test_mail_inbox(self):
        assert len(mail.outbox) == 0

        # assert example ==True

    def test_clinton_madien_name(self):
        assert self.clinton.madien_name == "Blythe III"

    def test_reagan_date_of_birth(self):
        assert self.reagan.date_of_birth == date(1911, 2, 6)

    def test_reagan_date_of_death(self):
        assert self.reagan.date_of_death == date(2004, 6, 5)

    def test_trump_password_meets_owasp_214_emoji_standard(self):
        """OWASP 2.1.4"""
        login_valid = self.trump.check_password(raw_password)
        assert login_valid == True

    def test_reagan_date_of_death(self):
        assert self.reagan.date_of_death == date(2004, 6, 5)

    def test_reagan_handle_deceased_is_active(self):
        assert self.reagan.is_active == False

    def test_reagan_mark_retention_only(self):
        assert self.reagan.retention_only == True

    def test_user_mark_retention_only(self):
        assert self.staff_user.retention_only == False

    def test_user_profile_first_name(self):
        assert self.staff_user.first_name == "Joseph"

    def test_user_profile_middle_name(self):
        assert self.staff_user.middle_name == "Robinette"

    def test_user_profile_full_name(self):
        assert self.staff_user.full_name == " Joseph Robinette Biden Jr"

    def test_user_profile_last_name(self):
        assert self.staff_user.last_name == "Biden"

    def test_user_profile_suffix(self):
        assert self.staff_user.suffix == "Jr"

    def test_user_profile_password(self):
        assert self.staff_user.password == hashed

    def test_user_profile_username(self):
        assert self.staff_user.username == "joseph.robinette.biden.jr"

    def test_user_profile_email(self):
        assert self.staff_user.email == "joseph.robinette.biden.jr@us.presidents.com"

    def test_profile_image(self):
        assert self.profile.image.name == "default.webp"

    def test_profile_internal_notes(self):
        assert self.profile.internal_notes == ""

    def test_is_staff(self):
        assert self.staff_user.is_staff == True

    def test_is_active(self):
        assert self.staff_user.is_active == True

    def test_is_patient(self):
        assert self.staff_user.is_patient == True

    def test_date_of_birth(self):
        assert self.staff_user.date_of_birth == date(1942, 11, 20)

    def test_is_clinic_staff(self):
        assert self.staff_user.is_clinic_staff == False

    def test_address_idempotent_key(self):

        assert self.address.idempotent_key == "ckpfzqd7l0000nbve3vq1hfgl"

    def test_address_address_type(self):
        assert self.address.address_type == "RESD"

    def test_address_street1(self):
        assert self.address.street1 == "1600 Pennsylvania Avenue NW"

    def test_address_street2(self):
        assert self.address.street2 == ""

    def test_address_state(self):
        assert self.address.state == "Washington"

    def test_address_city(self):
        assert self.address.city == "DC"

    def test_address_zipcode(self):
        assert self.address.zipcode == "20500"
