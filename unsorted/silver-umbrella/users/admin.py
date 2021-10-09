from django.contrib.admin import StackedInline, site
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import Address, Profile

User = get_user_model()


class AddressInline(StackedInline):
    model = Address
    can_delete = False


class ProfileInline(StackedInline):
    model = Profile
    can_delete = False
    inlines = (AddressInline,)


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    (
                        "username",
                        "email",
                        "password",
                    ),
                    (
                        "title",
                        "suffix",
                        "first_name",
                        "middle_name",
                        "last_name",
                    ),
                )
            },
        ),
        (
            "Advanced options",
            {
                "classes": ("collapse",),
                "fields": (
                    (
                        "date_of_birth",
                        "date_of_death",
                    ),
                    (
                        "is_patient",
                        "is_authorized_party",
                        "is_clinic_staff",
                    ),
                ),
            },
        ),
    )


site.register(User, UserAdmin)
