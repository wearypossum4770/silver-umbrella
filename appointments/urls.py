from django.urls import path

from appointments.views import (
    api_edit_or_create_appointment_by_patient_id,
    appointment_details,
    cancel_appointment_by_appointment_id,
    view_appointments,
    view_archived_appointments,
)

urlpatterns = [
    path(
        "appointments/<int:patient_id>/archive/",
        view_archived_appointments,
        name="appt-archive",
    ),
    path(
        "appointments/<appointment_id/cancel/",
        cancel_appointment_by_appointment_id,
        name="appt-cancel",
    ),
    path("appointments/<appointment_id>/", appointment_details, name="appt-detail"),
    path(
        "appointments/schedule-appointment/<int:patient_id>",
        api_edit_or_create_appointment_by_patient_id,
        name="new-appt",
    ),
    path("appointments/", view_appointments, name="appt-list"),
]
