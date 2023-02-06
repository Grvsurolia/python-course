from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to="products")
    description = models.TextField()
    mfg_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name