# Generated by Django 5.0.1 on 2024-01-20 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_location_coordinatesx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routes',
            name='time',
            field=models.IntegerField(),
        ),
    ]
