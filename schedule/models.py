from django.db import models


class Schedule(Model):
    class PeriodType(IntegerChoices):
        DAYS
        WEEKS
        MONTHS
        YEARS

    class Frequency(IntegerChoices):
        DAYS
        WEEKS
        MONTHS
        YEARS

    start_date
    start_time
    end_date
    end_time
