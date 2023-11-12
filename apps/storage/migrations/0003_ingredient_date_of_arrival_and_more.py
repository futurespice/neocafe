# Generated by Django 4.2.7 on 2023-11-11 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("storage", "0002_ingredient_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="ingredient",
            name="date_of_arrival",
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="composition",
            name="ingredient",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="compositions",
                related_query_name="composition",
                to="storage.ingredient",
            ),
        ),
        migrations.AlterField(
            model_name="composition",
            name="item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="compositions",
                related_query_name="composition",
                to="storage.item",
            ),
        ),
    ]
