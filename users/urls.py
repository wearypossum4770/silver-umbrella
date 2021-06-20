from django.contrib.auth import views
from django.urls import path

from users.views import about, homepage, profile, registration

urlpatterns = [
    path("", homepage, name="homepage"),
    path("about/", about, name="about"),
    path("profile/", profile, name="profile"),
    path("register/", registration, name="register"),
    path(
        "login/",
        views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path(
        "password-reset/",
        views.PasswordResetView.as_view(template_name="users/password_reset.html"),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
