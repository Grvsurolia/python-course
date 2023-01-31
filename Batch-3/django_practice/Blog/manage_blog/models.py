from django.db import models
from django.contrib.auth.models import User, AbstractUser


class CustomUser(AbstractUser):
    age = models.IntegerField()

    def __str__(self):
        return self.username


class Blog(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs")
    content = models.TextField()
    writer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

