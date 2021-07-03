from crispy_forms.helper import FormHelper
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField, ModelForm, ModelMultipleChoiceField

from users.models import Address, Profile

User = get_user_model()


def handle_save_address(user, **kwargs):
    address = user.profile.addresses.all().filter(
        idempotent_key=kwargs.get("idempotent_key")
    )[0]
    address_type = kwargs.get("address_type")
    street1 = kwargs.get("street1")
    street2 = kwargs.get("street2")
    state = kwargs.get("state")
    city = kwargs.get("city")
    zipcode = kwargs.get("zipcode")
    if address_type is not None:
        address.address_type = address_type
    if street1 is not None:
        address.street1 = street1
    if street2 is not None:
        address.street2 = street2
    if state is not None:
        address.state = state
    if city is not None:
        address.city = city
    if zipcode is not None:
        address.zipcode = zipcode
    address.save()


class AddressForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = Address
        fields = (
            "address_type",
            "street1",
            "street2",
            "state",
            "city",
            "zipcode",
        )


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    email = EmailField()

    class Meta:
        model = User
        fields = (
            "email",
            "username",
            "nickname",
            "first_name",
            "last_name",
            "middle_name",
            "title",
            "honorific_prefix",
            "honorific_suffix",
            "suffix",
            "date_of_birth",
            "password1",
            "password2",
        )


class UserUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    email = EmailField()

    class Meta:
        model = User
        fields = (
            "title",
            "first_name",
            "middle_name",
            "last_name",
            "suffix",
            "email",
            "nickname",
            "honorific_prefix",
            "honorific_suffix",
        )


class ProfileUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = Profile
        fields = (
            "image",
            "addresses",
        )
