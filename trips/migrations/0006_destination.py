# Generated by Django 4.0.6 on 2022-07-29 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0005_remove_transport_is_active_transport_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=120)),
                ('arrive_date', models.DateField(null=True)),
                ('depart_date', models.DateField(null=True)),
            ],
        ),
    ]
