# Generated by Django 3.2.4 on 2021-07-03 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_profile_birth_state"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="birth_state",
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]