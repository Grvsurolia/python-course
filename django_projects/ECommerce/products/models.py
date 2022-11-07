from django.db import models

from django.db import models
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length= 200, db_index = True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length =200)  
    image =models.ImageField(upload_to ='products/')
    description =models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available =models.BooleanField(default= True)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now =True)

    class meta:
        ordering =('-created')

    def __str__(self):
        return self.name

     