# Generated by Django 5.0.1 on 2024-04-01 18:08

import transaction.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0005_rename_interest_cashin_interrest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashin',
            name='interrest',
            field=models.JSONField(default=transaction.models.default_json_value),
        ),
    ]
