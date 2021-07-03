from django.urls import path

from blog.views import download_file
from leads.views import DetailView, IndexView, view_pdf

urlpatterns = [
    path("", IndexView.as_view(), name="leads"),
    path("<slug:pk>/", DetailView.as_view(), name="lead-detail"),
    path("employment/job_applications/%Y/%m/%d/", view_pdf, name="pdf-viewer"),
]
