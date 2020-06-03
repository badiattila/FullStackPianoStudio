from django.db import models

# Create your models here.
class Pianos(models.Model):
    brand = models.CharField(max_length=254, default='')
    price = models.DecimalField(max_digits=5, decimal_places=0)
    age = models.DecimalField(max_digits=3, decimal_places=0)
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.brand