from django.forms import ModelForm

from leads.models import Lead

# https://www.valentinog.com/blog/django-widgets/


class LeadForm(ModelForm):
    class Meta:
        model = Lead
        fields = "__all__"
        widgets = {"application_status": Textarea(attrs={})}
