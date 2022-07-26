# Generated by Django 4.0.6 on 2022-07-29 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_transport_trip_is_active_trip_transport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transport',
            name='is_active',
        ),
        migrations.AddField(
            model_name='transport',
            name='type',
            field=models.CharField(choices=[('DEFAULT', ''), ('AIR', 'Airplane'), ('TRAIN', 'Train'), ('BOAT', 'Boat'), ('BUS', 'Bus'), ('CAR', 'Car')], default='DEFAULT', max_length=25),
        ),
        migrations.AlterField(
            model_name='trip',
            name='description',
            field=models.TextField(max_length=255),
        ),
    ]
