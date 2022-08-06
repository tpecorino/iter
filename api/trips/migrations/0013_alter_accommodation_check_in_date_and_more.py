# Generated by Django 4.0.6 on 2022-08-06 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0012_remove_trip_destinations_trip_destinations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodation',
            name='check_in_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='check_out_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='reservation_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='destination',
            name='arrive_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='destination',
            name='depart_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='site',
            name='address_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='transport',
            name='arrive',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='transport',
            name='depart',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='transport',
            name='info_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='destinations',
            field=models.ManyToManyField(null=True, to='trips.destination'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='trip',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_date',
            field=models.DateField(),
        ),
    ]
