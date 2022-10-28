from distutils.command.upload import upload
from django.db import models

class Blog(models.Model):
    LANGUAGE_CHOICE = [
        ('english','ENGLISH'),
        ('hindi','HINDI'),
    ]
    blog_name = models.CharField(max_length = 100)
    blog_content = models.TextField()
    image = models.ImageField(upload_to="blog/")
    blog_date = models.DateField()
    language = models.CharField(max_length = 20, choices=LANGUAGE_CHOICE)

    def __str__(self):
        return self.blog_name