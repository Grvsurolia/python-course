# Generated by Django 4.1.3 on 2023-03-02 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon_time', '0004_bookings_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
