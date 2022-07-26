# Generated by Django 4.0.6 on 2022-08-06 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0019_alter_transportation_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accommodation',
            old_name='destination_id',
            new_name='destination',
        ),
        migrations.RenameField(
            model_name='destination',
            old_name='trip_id',
            new_name='trip',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='destination_id',
            new_name='destination',
        ),
        migrations.RenameField(
            model_name='transportation',
            old_name='destination_id',
            new_name='destination',
        ),
    ]
