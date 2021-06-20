from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField, ModelForm

from .models import Profile

User = get_user_model()


class UserRegisterForm(UserCreationForm):
    email = EmailField()

    class Meta:
        model = User
        fields = (
            "nickname",
            "first_name",
            "last_name",
            "middle_name",
            "email",
            "username",
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
            "date_of_birth",
            "is_patient",
            "is_clinic_staff",
            "date_of_death",
            "retention_only",
            "do_not_contact",
            "password",
        )


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = (
            "image",
            "addresses",
        )
