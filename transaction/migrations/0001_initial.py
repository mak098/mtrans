# Generated by Django 5.0.1 on 2024-03-10 15:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Agency', '0011_remove_agency_detail_agency_address_agency_phone'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CashIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=350, verbose_name='Code')),
                ('amount', models.FloatField(default=0.0, verbose_name='Amount')),
                ('sender', models.CharField(max_length=350, verbose_name='Sender')),
                ('sender_phone', models.CharField(max_length=50, verbose_name='Sender phone')),
                ('recipient', models.CharField(max_length=350, verbose_name='Recipient')),
                ('recipient_phone', models.CharField(max_length=350, verbose_name='Recipient phone')),
                ('comment', models.TextField(blank=True, max_length=200, null=True, verbose_name='Comment')),
                ('status', models.BooleanField(default=False, verbose_name='is served')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transaction_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('interrest', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='interrest_rate', to='Agency.interrestrateconfig', verbose_name='Destination')),
            ],
            options={
                'verbose_name_plural': 'cash In',
            },
        ),
        migrations.CreateModel(
            name='CashOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0, verbose_name='Amount')),
                ('recipient', models.CharField(max_length=350, null=True, verbose_name='Recipient')),
                ('recipient_phone', models.CharField(max_length=350, null=True, verbose_name='Recipient phone')),
                ('comment', models.TextField(blank=True, max_length=200, null=True, verbose_name='Comment')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cash_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='transaction_cashout', to='transaction.cashin', verbose_name='Transaction')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transaction_cashout_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
            ],
            options={
                'verbose_name_plural': 'Cash out',
            },
        ),
        migrations.CreateModel(
            name='Interrest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0, verbose_name='Amount')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cash_in', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='transaction_interrest', to='transaction.cashin', verbose_name='Transaction')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transaction_interrest', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
            ],
            options={
                'verbose_name_plural': 'Interests',
            },
        ),
    ]
