# Generated by Django 4.0.6 on 2022-07-28 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_alter_trip_description_alter_trip_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
