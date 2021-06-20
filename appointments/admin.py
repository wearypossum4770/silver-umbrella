from django.contrib import admin

from appointments.models import Appointment, Patient


def view_clinic_appointments(request, show_is_archived=False):
    ...


def view_patient_appointments(request, show_is_archived=False):
    ...


def create_patient_appointment(request):
    ...


admin.site.register(Appointment)
admin.site.register(Patient)
