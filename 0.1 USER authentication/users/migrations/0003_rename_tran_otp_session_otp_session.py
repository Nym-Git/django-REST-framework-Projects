# Generated by Django 4.0.3 on 2022-07-27 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_tran_otp_session'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tran_Otp_Session',
            new_name='otp_session',
        ),
    ]
