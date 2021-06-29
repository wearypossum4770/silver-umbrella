from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField, ModelForm

from users.models import Address, Profile

User = get_user_model()


def handle_save_address(user, **kwargs):
    address = user.profile.addresses.all().filter(
        idempotent_key=kwargs.get("idempotent_key")
    )[0]
    address.address_type = kwargs.get("address_type")
    address.street1 = kwargs.get("street1")
    address.street2 = kwargs.get("street2")
    address.state = kwargs.get("state")
    address.city = kwargs.get("city")
    address.zipcode = kwargs.get("zipcode")
    address.save()


class AddressForm(ModelForm):
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
    email = EmailField()

    class Meta:
        model = User
        fields = (
            "nickname",
            "first_name",
            "last_name",
            "middle_name",
            "title",
            "honorific_prefix",
            "honorific_suffix",
            "suffix",
            "password",
        )


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = (
            "image",
            "addresses",
        )
