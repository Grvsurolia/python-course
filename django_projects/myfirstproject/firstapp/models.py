from django.db import models


class Course(models.Model):
    SECTION_CHOICE = [
        ('a','A'),
        ('b','B'),
        ('c','C'),
    ]
    course_name = models.CharField(max_length = 100)
    active = models.BooleanField(default=True)
    date = models.DateField()
    current_time = models.DateTimeField()
    section = models.CharField(max_length = 20, choices=SECTION_CHOICE)


class Student_details(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50, blank=True)