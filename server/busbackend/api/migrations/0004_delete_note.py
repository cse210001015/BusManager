# Generated by Django 4.1.3 on 2024-01-20 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_bookings_fromstop_alter_bookings_tostop'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Note',
        ),
    ]
