# Generated by Django 4.0.6 on 2022-07-30 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0010_alter_destination_accommodations_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='additional_resources',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]