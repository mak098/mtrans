# Generated by Django 5.0.1 on 2024-01-30 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'verbose_name_plural': 'Transactions'},
        ),
        migrations.AlterModelOptions(
            name='wallet',
            options={'verbose_name_plural': 'Wallets'},
        ),
    ]