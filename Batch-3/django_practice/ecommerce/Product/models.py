from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to="products")
    description = models.TextField()

    def __str__(self):
        return self.name