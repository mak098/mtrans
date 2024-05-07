# Generated by Django 5.0.1 on 2024-05-05 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0007_rename_interrest_cashin_distribution'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashin',
            name='recipient_id_or_passport',
            field=models.CharField(default='-', max_length=350, null=True, verbose_name='ID or Passport '),
        ),
        migrations.AddField(
            model_name='cashin',
            name='sender_id_or_passport',
            field=models.CharField(default='-', max_length=350, null=True, verbose_name='Sender ID or Passport '),
        ),
        migrations.AddField(
            model_name='cashout',
            name='recipient_id_or_passport',
            field=models.CharField(default='-', max_length=350, null=True, verbose_name='ID or Passport '),
        ),
    ]