# Generated by Django 4.0.6 on 2022-07-29 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0006_destination'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='destinations',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trips.destination'),
        ),
    ]