# Generated by Django 3.2.8 on 2021-11-01 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('degreed2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='degreed2enterprisecustomerconfiguration',
            old_name='key',
            new_name='client_id',
        ),
        migrations.RenameField(
            model_name='degreed2enterprisecustomerconfiguration',
            old_name='secret',
            new_name='client_secret',
        ),
        migrations.RenameField(
            model_name='historicaldegreed2enterprisecustomerconfiguration',
            old_name='key',
            new_name='client_id',
        ),
        migrations.RenameField(
            model_name='historicaldegreed2enterprisecustomerconfiguration',
            old_name='secret',
            new_name='client_secret',
        ),
    ]
