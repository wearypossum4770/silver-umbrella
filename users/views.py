from cuid import cuid
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from users.forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm
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
    form = UserRegisterForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request,
                f" {username} Your account has been created! You are now able to log in",
            )
            return redirect("login")
    return render(request, "users/register.html", {"form": form})


def handle_addresses(user, *args, **kwargs):
    addr = Profile.objects.get(user=user)
    print(user)
    print(addr)


@login_required
def profile(request):
    data = request.POST
    user = request.user
    handle_addresses(request.user)
    user_form = UserUpdateForm(data, instance=user)
    profile_form = ProfileUpdateForm(data, request.FILES, instance=user.profile)
    if request.method == "POST":
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save() and profile_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("profile")
    context = {"user_form": user_form, "profile_form": profile_form}
    return render(request, "users/profile.html", context)
