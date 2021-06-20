from datetime import datetime
from uuid import uuid4

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKey,
    ManyToManyField,
    Model,
    TextChoices,
    TextField,
    UUIDField,
)
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _

BASE_DIR = settings.BASE_DIR
User = get_user_model()
__gender__ = {
    "M": "I identify as a male or a man (i.e. male, cis-gender male), and prefer to be called sir",
    "F": "I identify as a female or a woman (i.e. female, cis-gender female),  and prefer to be called ma'am.",
    "MTF": "Assigned male at birth, but currently identify as female.",
    "FTM": "Assigned female at birth but currently identify as male.",
    "NBN": "Neither male nor female, somewhere in between.",
    "none": "No Selection, Declined To Answer",
}
__ethnicity__ = {
    "ASN": "Asian - Far East, Southeast Asia, or the Indian subcontinent including, for example, Cambodia, China, India, Japan, Korea, Malaysia, Pakistan, the Philippine Islands, Thailand, and Vietnam.",
    "BLK": "Black - origins in any of the Black racial groups of Africa including Carribean Islands.",
    "NAT": "Native American or Alaskan Native.",
    "HPN": "Hispanic - Centeral and South America, Carribbean Islands.",
    "MDE": "Middle Eastern - the Middle East, or North Africa.",
    "HWN": "Native Hawaii, Guam, Samoa, or other Pacific Islands.",
    "OTH": "Other/Multiple",
    "WHT": "White-origins in Europe.",
    "none": "No Selection, Declined To Answer",
}
__relationship__ = {
    "GAR": "Legal guardian",
    "KIN": "Next of kin or emergency contact",
    "PAR": "Includes both custodial, non-custodial, foster, and step parents.",
    "LAW": "",
}


class Appointment(Model):
    class Action(TextChoices):
        COMPLETE = "CMPL", _("Completed")
        CANCELLED = "CAND", _("Canelled")
        SCHEDULED = "SCHD", _("Scheduled")
        IN_PROGRESS = "INPR", _("In Progress")
        __empty__ = "('UNKNOWN')"

    patient = ForeignKey(User, on_delete=CASCADE, related_name="appointment_for")
    scheduler = ForeignKey(User, on_delete=CASCADE, related_name="created_by")
    scheduled_time = DateTimeField(auto_now_add=True, null=True, blank=True)
    date_modified = DateTimeField(auto_now=True, null=True, blank=True)
    start_time = DateTimeField(null=True, blank=True)
    end_time = DateTimeField(null=True, blank=True)
    location = CharField(max_length=20, null=True, blank=True)
    visit_identifier = UUIDField(default=uuid4, unique=True)
    action_status = CharField(
        max_length=4, default=Action.__empty__, choices=Action.choices
    )
    external_identifier = CharField(max_length=100, null=True, blank=True)
    is_archived = BooleanField(default=False, null=True, blank=True)
    date_archived = DateTimeField(default=None, null=True, blank=True)
    soft_delete = BooleanField(default=False, null=True, blank=True)
    is_deleted = BooleanField(default=False, null=True, blank=True)
    deleted_at = DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.patient.username

    @property
    def mark_as_completed(self):
        ...

    @property
    def mark_as_missed(self):
        ...

    def mark_as_clinic_cancellation(self):
        """ADMIN only view"""
        ...

    def mark_as_authorized_party_cancellation(self):
        ...

    def mark_as_clinic_conflict(self):
        ...

    def mark_schedule_as_next_avaiable(self):
        ...

    @property
    def mark_as_inprogress(self):
        ...

    @property
    def mark_as_unarchived(self):
        self.is_archived = False
        if self.date_archived:
            self.date_archived = None

    @property
    def mark_as_archived(self):
        self.is_archived = True
        self.date_archived = datetime.now()

    @property
    def mark_as_deleted(self):
        ...

    @property
    def mark_as_undeleted(self):
        ...


# Tech support
class AuthorizedParty(Model):
    class Relationship(TextChoices):
        GUARDIAN = "GAR", _(f"{__relationship__.get('GAR')}")
        PARENT = "PAR", _(f"{__relationship__.get('PAR')}")
        LEGAL_ADVISOR = "LAW", _(f"{__relationship__.get('LAW')}")
        EMERGENCY = "KIN", _(f"{__relationship__.get('KIN')}")

    owner = ForeignKey(User, on_delete=CASCADE)


class Patient(Model):
    """
    United States Census Beurau Ethnicity Information. https://www.census.gov/topics/population/race/about.html
    Improved Ethinicity Information. https://www2.census.gov/cac/nac/meetings/2016-10/2016-nac-jones.pdf
    """

    class Gender(TextChoices):
        MALE = "M", _(f"{__gender__.get('M')}")
        FEMALE = "F", _(f"{__gender__.get('F')}")
        TRANSGENDER_FEMALE = "MTF", _(f"{__gender__.get('MTF')}")
        TRANSGENDER_MALE = "FTM", _(f"{__gender__.get('FTM')}")
        NON_BINARY = "NBN", _(f"{__gender__.get('NBN')}")
        __empty__ = _(f"{__gender__.get('none')}")

    class Ethnicity(TextChoices):
        ASIAN = "ASN", _(f"{__ethnicity__.get('ASN')}")
        BLACK = "BLK", _(f"{__ethnicity__.get('BLK')}")
        Native = "NAT", _(f"{__ethnicity__.get('NAT')}")
        HISPANIC = "HPN", _(f"{__ethnicity__.get('HPN')}")
        MIDDLE_EASTERN = "MDE", _(f"{__ethnicity__.get('MDE')}")
        HAWAIIAN = "HWN", _(f"{__ethnicity__.get('HWN')}")
        OTHER = "OTH", _(f"{__ethnicity__.get('OTH')}")
        WHITE = "WHT", _(f"{__ethnicity__.get('WHT')}")
        __empty__ = _(f"{__ethnicity__.get('none') }")

    owner = ForeignKey(User, on_delete=CASCADE, related_name="patient")
    authorized_party = ManyToManyField(User, related_name="authorized_party")
    sponsor = ForeignKey(User, on_delete=CASCADE, related_name="guarantor")
    gender = CharField(
        max_length=3,
        choices=Gender.choices,
        default=Gender.__empty__,
    )
    ethnicity = CharField(
        max_length=3, choices=Ethnicity.choices, default=Ethnicity.__empty__
    )
    internal_notes = TextField(null=True, blank=True)

    def __str__(self):
        return self.owner.username

    def user_can_manage_me(self, owner):
        return owner == self.owner or owner.has_perm("your_app.manage_object")


class MedicalCondition(Model):
    """
    Check out this page https://www.cdc.gov/nchs/icd/icd9cm_addenda_guidelines.htm
    also https://www.aappublications.org/news/2020/05/07/coding050720?utm_source=TrendMD&utm_medium=TrendMD&utm_campaign=AAPNews_TrendMD_0
    """

    class System(TextChoices):
        TEN = "icd_10", _("ICD 10 Code (international classification of diseases)")
        NINE = "icd_9", _("ICD 9 Code (international classification of diseases)")

    class Classification(TextChoices):
        CM = "CM", _("Clinical Modification")
        PCS = "PCS", _("Procedure Coding System")
        HCPCS = "HCP", _("Healthcare Common Procedure Coding System")
        CPT = "CPT", _("Current Procedural Terminology")

    signature_required = BooleanField(default=False, null=True, blank=True)
    blue_ink_required = BooleanField(default=False, null=True, blank=True)
    enrollment_required = BooleanField(default=False, null=True, blank=True)
    is_symptomatic = BooleanField(default=False, null=True, blank=True)
    code_value = CharField(max_length=15, null=True, blank=True)
    coding_system = CharField(
        max_length=6, choices=System.choices, default=System.TEN, null=True, blank=True
    )
    has_category_code = CharField(
        max_length=3, choices=Classification.choices, null=True, blank=True
    )
    used_to_diagnose = CharField(max_length=100, null=True, blank=True)
    condition_description = CharField(max_length=200, null=True, blank=True)
    related_condition = CharField(max_length=200, null=True, blank=True)


# https://www.callcentrehelper.com/tag/workforce-management
# class ConatctLog(Model):
#     class Disposition(TextChoices):
#         ABANDONED = "", _("Caller abandoned in queue")
#         SCHEDULED = "SCH", _("Caller qppointment scheduled")
#         BUSY= "BSY", _("Line Busy")
#         CALLBACK= "CBK", _("Caller request, callback")
#         COMPLAINT = "CMP", _("Caller wishes to file Complaint/Greievnance")
#         COMPLETE = "CPT"
# class Type:
#     INBOUND
#     OUTBOUND
#     WARM_TRANSFER
#     COLD_TRANSFER
# class NextAction:
# outcome = CharField(max_length=100, null=True, blank=True)

# Complete
# Disconnected number
# Incorrect number
# Not interested
# Product question
# Requires follow up
# Requires supervisor attention
# ADMIN = "ADMIN", _("Administration")
# AGRMT = "AGRMT", _("Agreement")
# AOF = "AOF", _("Address on File")
# AOS = "AOS", _("Already on System")
# APVL = "APVL", _("Approval")
# ATTM = "ATTM", _("At this time")
# AUTH = "AUTH", _("Authority, authorise")
# CB = "CB", _("or CL BK, Call back")
# CC = "CC", _("Customer care")
# CCI = "CCI", _("Customer called in")
# CIN = "CIN", _("Customer I/D number")
# CCM = "CCM", _("Customer Care Manager")
# CMPLT = "CMPLT", _("Complete")
# CNL = "CNL", _("Cancel")
# CONF = "CONF", _("Confidential")
# COT = "COT", _("Change of title")
# CSM = "CSM", _("Customer Service Manager")
# CTI = "CTI", _("Customer telephoned in")
# CUST = "CUST", _("Customer")
# CUST_SUPP = "CUST_SUPP", _("Customer Support")
# DD = "DD", _("Direct debit")
# DESTN = "DESTN", _("Destination")
# DET = "DET", _("Detail(s)")
# DLVY = "DLVY", _("Delivery")
# DPA = "DPA", _("Data Protection Act")
# EDD = "EDD", _("Expected date of delivery")
# EMERG = "EMERG", _("Emergency")
# ENRT = "ENRT", _("En route")
# EST = "EST", _("Estimate or estimation")
# EVAL = "EVAL", _("Evaluate or evaluation")
# EXTN = "EXTN", _("Extension")
# FAO = "FAO", _("For attention of")
# FONE = "FONE", _("Telephone")
# FTE = "FTE", _("Full-time equivalent")
# IAW = "IAW", _("In accordance with")
# IDENT = "IDENT", _("Identify or identifier or identification")
# IMPT = "IMPT", _("Important")
# IMT = "IMT", _("Immediate or immediately")
# INFO = "INFO", _("Information")
# K = "K", _("Thousand")
# MAX = "MAX", _("Maximum")
# MISG = "MISG", _("Missing")
# MULT = "MULT", _("Multiple")
# NA = "N/A", _("Not applicable")
# NAP = "NAP", _("Not at present")
# NC = "NC", _("No change")
# NIS = "NIS", _("Not in system")
# NOAC = "NOAC", _("No action necessary")
# NOFIN = "NOFIN", _("No further information")
# NT = "NT", _("No trace")
# ON_file = "O/F", _("On file")
# OVERPAYMENT = "O/P", _("Overpayment")
# ON_request = "O/R", _("On request")
# OTS = "OTS", _("Out of service")
# PH = "PH", _("Past history")
# PI = "PI", _("Personal issue")
# PO = "PO", _("Purchase order")
# PYT = "PYT", _("Payment")
# QLTY = "QLTY", _("Quality")
# QNTY = "QNTY", _("Quantity")
# RECD = "RECD", _("Received")
# RE = "RE", _("In regard to")
# REQD = "REQD", _("Required")
# REQSTD = "REQSTD", _("Requested")
# RETN = "RETN", _("Return/Returned")
# RFC = "RFC", _("Request for change")
# RPRT = "RPRT", _("Report")
# SATFY = "SATFY", _("Satisfy or satisfactory")
# SC = "SC", _("Sort Code")
# SDBY = "SDBY", _("Standby")
# SGD = "SGD", _("Signed")
# SLA = "SLA", _("Service Level Agreement")
# SO = "SO", _("Standing order")
# SP = "SP", _("Single payment")
# SUP = "SUP", _("Supply")
# SUSP = "SUSP", _("Suspend")
# SYS = "SYS", _("System")
# TEMP = "TEMP", _("Temporary")
# TOC = "TOC", _("To be continued")
# TOD = "TOD", _("Time of delivery")
# TOR = "TOR", _("Time of receipt")
# TRANSCODE = "TRANSCODE", _("Transaction code")
# TRMT = "TRMT", _("Terminate")
# UNAPV = "UNAPV", _("Unable to approve")
# UNAVBL = "UNAVBL", _("Unavailable")
# UNDLD = "UNDLD", _("Undelivered")
# URG = "URG", _("Urgent")
# UNSATFY = "UNSATFY", _("Unsatisfactory")
# WEF = "WEF", _("With effect from")
# WIBIS = "WIBIS", _("Will be issued")
# WIP = "WIP", _("Work in progress")
# WISMO = "WISMO", _("Where is my order?")
