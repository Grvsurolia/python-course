# Generated by Django 4.1.5 on 2023-01-30 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(blank=True),
        ),
    ]
