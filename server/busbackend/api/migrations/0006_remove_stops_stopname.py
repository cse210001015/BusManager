# Generated by Django 4.1.3 on 2024-01-20 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_delete_seats_rename_busid_bookings_busid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stops',
            name='stopName',
        ),
    ]
