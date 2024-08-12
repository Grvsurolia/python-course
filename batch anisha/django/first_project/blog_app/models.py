from django.db import models

class Blog_data(models.Model):
    title = models.CharField(max_length=10)
    writer = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images', null=True, blank=True)

    def __str__(self):
        return self.title