# Generated by Django 5.0.1 on 2024-02-03 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agency', '0010_alter_interrestrateconfig_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agency',
            name='detail',
        ),
        migrations.AddField(
            model_name='agency',
            name='address',
            field=models.CharField(blank=True, max_length=350, null=True, verbose_name='Adress'),
        ),
        migrations.AddField(
            model_name='agency',
            name='phone',
            field=models.CharField(blank=True, max_length=350, null=True, verbose_name='Phone'),
        ),
    ]
