import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("users.urls")),
    path("", include("appointments.urls")),
    path("", include("blog.urls")),
    path("__debug__/", include(debug_toolbar.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
