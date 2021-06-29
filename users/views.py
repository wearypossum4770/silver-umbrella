from cuid import cuid
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from users.forms import AddressForm, ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from users.models import Address, Profile

address_switcher = {
    "MAIL": "Mailing",
    "RESD": "Residential",
    "BUSN": "Business",
}


def homepage(request):
    return render(request, "users/home.html")


def about(request):
    return render(request, "users/about.html")


def registration(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Your account has been created! You are now able to log in"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


def handle_get_addresses(user, idempotent_key=None):
    addresses = user.profile.addresses.all()
    return addresses.get(idempotent_key=idempotent_key) if idempotent_key else addresses


@login_required
def profile(request):
    _user = request.user
    addresses = handle_get_addresses(_user)
    if request.method == "POST":
        _files = request.FILES
        _data = request.POST
        user_form = UserUpdateForm(_data, instance=_user)
        profile_form = ProfileUpdateForm(_data, _files, instance=_user.profile)
        address_form = AddressForm(_data)
        if user_form.is_valid():
            user_form.save()
        if profile_form.is_valid():
            profile_form.save()
        messages.success(request, f"Your account has been updated!")
        return redirect("profile")
    else:
        address_form = AddressForm(instance=_user.profile)
        user_form = UserUpdateForm(instance=_user)
        profile_form = ProfileUpdateForm(instance=_user.profile)
    print(addresses)
    return render(
        request,
        "users/profile.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
            "address_form": address_form,
            "addresses": addresses,
        },
    )
