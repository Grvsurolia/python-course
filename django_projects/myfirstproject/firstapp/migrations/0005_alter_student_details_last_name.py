# Generated by Django 4.1.2 on 2022-10-20 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_student_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_details',
            name='last_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
