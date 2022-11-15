# Generated by Django 4.0.6 on 2022-07-30 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0011_alter_site_additional_resources'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='destinations',
        ),
        migrations.AddField(
            model_name='trip',
            name='destinations',
            field=models.ManyToManyField(blank=True, to='trips.destination'),
        ),
    ]