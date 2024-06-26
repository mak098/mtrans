# Generated by Django 5.0.1 on 2024-01-30 18:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agency', '0004_alter_agency_created_by_alter_firm_created_by_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='interrestrateconfig',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='rated_by', to=settings.AUTH_USER_MODEL, verbose_name='Config by'),
        ),
    ]
