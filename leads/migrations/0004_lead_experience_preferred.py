# Generated by Django 3.2 on 2021-05-04 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("leads", "0003_alter_lead_employer_overview"),
    ]

    operations = [
        migrations.AddField(
            model_name="lead",
            name="experience_preferred",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]