# Generated by Django 4.1.2 on 2022-10-20 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_course_active_course_date_course_date_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='date_time',
            new_name='current_time',
        ),
    ]
