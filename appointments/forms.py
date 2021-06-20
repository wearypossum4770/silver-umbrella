from django.forms import EmailField, ModelForm

from appointments.models import Appointment


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = (
            "start_time",
            "end_time",
            "location",
        )

    def form_valid(self, form):
        form.instance.scheduler = self.request.user
        return super().form_valid(form)
