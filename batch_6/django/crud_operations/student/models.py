from django.db import models

class StudentDetails(models.Model):
    name = models.CharField(max_length=50)
    class_ = models.IntegerField()
    age = models.IntegerField()


class TeacherDetails(models.Model):
    name = models.CharField(max_length=50)
    salary = models.IntegerField()