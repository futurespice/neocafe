# Generated by Django 4.2.7 on 2023-11-09 06:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("branches", "0002_rename_phone_branch_phone_number"),
        ("accounts", "0009_remove_customuser_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="birth_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="bonus",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="customuser",
            name="branch",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="branches.branch",
            ),
        ),
        migrations.AddField(
            model_name="customuser",
            name="position",
            field=models.CharField(
                choices=[
                    ("barista", "Barista"),
                    ("waiter", "Waiter"),
                    ("client", "Client"),
                ],
                default="client",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="first_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="customuser_groups",
                related_query_name="customuser",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="last_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="customuser_permissions",
                related_query_name="customuser",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
        migrations.AlterField(
            model_name="phonenumberverification",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="phone_number_verifications",
                to="accounts.customuser",
            ),
        ),
    ]
