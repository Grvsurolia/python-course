from django.db import models

class Profile(models.Model):
    SUBJECT_CHOICE = [
        ('English',"ENGLISH"),
        ('hindi',"HINDI"),
    ]
    student_name = models.CharField(max_length=50)
    class_name = models.CharField(max_length = 50)
    roll_no = models.IntegerField()
    subject = models.CharField(max_length = 50, choices=SUBJECT_CHOICE)
    
    def __str__(self):
        return self.student_name