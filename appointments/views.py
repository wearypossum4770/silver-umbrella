from asgiref.sync import sync_to_async
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render

from appointments.forms import AppointmentForm
from appointments.models import Appointment, Patient

User = get_user_model()


def wrap_up_time():
    ...


def after_call_work():
    ...


def disposition_code():
    ...


def find_next_avaiable():
    ...


def user_can_manage_me(user):
    return user.has_perm("your_app.manage_object")


def user_is_authenticated(user):
    return user.is_authenticated


def user_is_patient(user):
    return user.is_patient


def user_is_clinic_staff(user):
    return user.is_clinic_staff


@login_required
@user_passes_test(user_is_authenticated)
def api_edit_or_create_appointment_by_patient_id(request, patient_id):
    context = {}
    _u = get_user_model().objects.get(pk=patient_id)
    patient = Patient.objects.get(owner=_u)
    user_is_authorized_party = (
        patient.authorized_party.all().filter(username=request.user.username).exists()
    )
    context.update(
        user_is_authorized_party=user_is_authorized_party,
    )
    if user_is_authorized_party:
        obj, created = Appointment.objects.get_or_create(
            patient_id=patient_id,
            scheduler_id=request.user.id,
            is_archived=False,
            location=request.POST.get("location"),
            start_time=request.POST.get("start_time"),
            end_time=request.POST.get("end_time"),
            visit_identifier=request.POST.get("visit_identifier"),
            action_status=Appointment.Action.SCHEDULED,
        )
        context.update(
            created=created,
            status_code=201,
            appointment_details={
                "visit_identifier": obj.visit_identifier,
                "scheduled_time": obj.scheduled_time,
                "start_time": obj.start_time,
                "end_time": obj.end_time,
                "location": obj.location,
                "action_status": obj.action_status,
            },
        )
        # if not obj.user_can_manage_me(request.user):
    return JsonResponse(context)


@login_required
@user_passes_test(user_is_authenticated)
def appointment_details(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id, is_archived=False)
    if appointment.patient.username == request.user.username:
        return JsonResponse(
            {
                "patient": appointment.patient.username,
                "scheduler": appointment.scheduler.username,
                "scheduled_time": appointment.scheduled_time,
                "start_time": appointment.start_time,
                "end_time": appointment.end_time,
                "location": appointment.location,
                "action_status": appointment.action_status,
            }
        )


@login_required
@user_passes_test(user_is_authenticated)
def view_archived(request):
    appointments = get_object_or_404(
        Appointment, owner=request.user.id, is_archived=True
    )
    archived_appointments = [
        {
            "patient": appt.patient.username,
            "scheduler": appt.scheduler.username,
            "scheduled_time": appt.scheduled_time,
            "start_time": appt.start_time,
            "end_time": appt.end_time,
            "location": appt.location,
            "action_status": appt.action_status,
        }
        for appt in appointments
    ]
    return JsonResponse({"archived_appointments": archived_appointments})


@login_required
@user_passes_test(user_is_authenticated)
def view_archived_appointments(request, patient_id):
    context = {}

    patient = Patient.objects.get(owner_id=patient_id)
    user_is_authorized_party = (
        patient.authorized_party.all().filter(username=request.user.username).exists()
    )
    context.update(
        user_is_authorized_party=user_is_authorized_party,
    )
    if user_is_authorized_party:
        appointments = get_list_or_404(Appointment, patient_id=patient_id)
        archived_appointments = [
            {
                "patient": appt.patient.username,
                "scheduler": appt.scheduler.username,
                "start_time": appt.start_time,
                "end_time": appt.end_time,
                "external_identifier": appt.external_identifier,
                "location": appt.location,
                "action_status": appt.action_status,
            }
            for appt in appointments
        ]
        context.update(archived_appointments=archived_appointments)
    return JsonResponse(context)


@login_required
@user_passes_test(user_is_authenticated)
def archive(request):
    context = {}
    return JsonResponse(context)


@login_required
@user_passes_test(user_is_authenticated)
def archive_appointment(request, appointment_id):
    appointment = get_object_or_404(
        Appointment, owner=request.user.id, pk=appointment_id
    )
    appointment.is_archived = True
    appointment.save()
    return appointment.is_archived


@login_required
@user_passes_test(user_is_authenticated)
def view_appointments(request):
    """
    Allows a patient or authorized user to view appointments
    """
    context = {}
    appt = Appointment.objects.filter(patient=request.user.id, is_archived=False)
    if request.user.is_authenticated:
        context["appointment_list"] = [
            {
                "scheduled_time": a.scheduled_time,
                "start_time": a.start_time,
                "end_time": a.end_time,
                "location": a.location,
                "action_status": a.action_status,
                "external_identifier": a.external_identifier,
            }
            for a in appt
        ]
    return JsonResponse(context)


@login_required
@user_passes_test(user_is_authenticated)
def cancel_appointment_by_appointment_id(
    request, appointment_id, cancel_appointment=False
):
    if cancel_appointment:
        appointment = get_object_or_404(Appointment, external_identifier=appointment_id)
        appointment.action_status = Appointment.Action.CANCELLED
        appointment.save()
    return appointment.action_status == Appointment.Action.CANCELLED


@login_required
@user_passes_test(user_is_authenticated)
def make_appointment(request, patient_id, *args, **kwargs):
    context = {}
    patient = Patient.objects.get(owner=patient_id)
    user_is_authorized_party = len(
        [
            user.username
            for user in patient.authorized_party.all()
            if user.username == request.user.username
        ]
    )

    return JsonResponse(context)


#  cancel_appointment_by_date_range
#  cancel_appointment_by_appointment_id
#  appointment_modification_notify_patient
#  create_appointment_by_patient_id
#  create_appointment_by_system
#  view_appointment_details_by_appointment_id
#  view_appointment_list_by_patient_id
#  view_appointment_list_by_date_range
#  view_current_day_appointment_list
#
