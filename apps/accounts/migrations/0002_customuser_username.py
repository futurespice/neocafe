# Generated by Django 4.2.7 on 2023-11-10 08:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="username",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
