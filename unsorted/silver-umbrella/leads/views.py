from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import DetailView, ListView

from leads.models import Lead


def view_pdf(request):
    return render(request, "blog/pdf_viewer.html")


def lead_detail_view(request, lead_id):
    """
    TemplateID 8ade75b4-9925-4350-a7e2-f78fa0e6222a
    """
    lead = get_object_or_404(Lead, pk=lead_id)
    return render(request, "leads/detail.html", {"lead": lead})


def lead_list_view(request):
    """
    TemplateID 8ade75b4-9925-4350-a7e2-f78fa0e6222a
    """
    leads_list = Lead.objects.all()
    return render(request, "leads/index.html", {"leads_list": leads_list})


def lead_list(request):
    leads = Lead.objects.all()
    return render(request, "leads/index.html", {"leads": leads})


def lead_view(request, lead_id):
    ...


def lead_create(request):
    ...


def lead_update(request, lead_id):
    ...


def lead_delete(request, lead_id):
    ...


class IndexView(ListView):
    model = Lead
    template_name = "leads/index.html"
    context_object_name = "lead_list"


class DetailView(DetailView):
    model = Lead
    template_name = "leads/detail.html"
