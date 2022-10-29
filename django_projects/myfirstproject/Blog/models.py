from distutils.command.upload import upload
from enum import unique
from django.db import models

class Blog(models.Model):
    LANGUAGE_CHOICE = [
        ('english','ENGLISH'),
        ('hindi','HINDI'),
    ]
    blog_name = models.CharField(max_length = 100, unique=True)
    blog_content = models.TextField()
    image = models.ImageField(upload_to="blog_images/", null=True, blank=True)
    blog_date = models.DateField()
    language = models.CharField(max_length = 20, choices=LANGUAGE_CHOICE)

    def __str__(self):
        return self.blog_name