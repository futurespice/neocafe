# Generated by Django 4.2.7 on 2023-11-13 06:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("branches", "0005_alter_branch_schedule_alter_workdays_schedule"),
    ]

    operations = [
        migrations.AddField(
            model_name="branch",
            name="name_of_shop",
            field=models.CharField(default="NeoCafe Dzerzhinka", max_length=100),
        ),
    ]