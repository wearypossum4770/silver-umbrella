# Generated by Django 3.2.3 on 2021-06-30 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_auto_20210630_1148"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="owasp_safe_password",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="prompt_password_change",
            field=models.BooleanField(default=False),
        ),
    ]