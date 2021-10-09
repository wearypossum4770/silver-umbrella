# Generated by Django 3.2.3 on 2021-07-06 02:18

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0008_auto_20210705_2143"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="user",
            name="not_dead_tomorrow",
        ),
        migrations.RemoveConstraint(
            model_name="user",
            name="born_before_today",
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.CheckConstraint(
                check=models.Q(("date_of_death__lte", datetime.date(2021, 7, 7))),
                name="not_dead_tomorrow",
            ),
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.CheckConstraint(
                check=models.Q(("date_of_birth__lte", datetime.date(2021, 7, 6))),
                name="born_before_today",
            ),
        ),
    ]