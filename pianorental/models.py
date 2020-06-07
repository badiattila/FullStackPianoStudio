from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PianosForRent(models.Model):
    brand = models.CharField(max_length=254, default='')
    price = models.DecimalField(max_digits=5, decimal_places=0)
    age = models.DecimalField(max_digits=3, decimal_places=0)
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    # Declaring loan status characters to be used in status field
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )
    at_user = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    rented_since = models.DateField()
    
    class Meta:
        ordering = ['price']    
    
    def __str__(self):
        return self.brand

class Payment(models.Model):
    payment_amount = models.DecimalField(max_digits=5, decimal_places=0)
    payment_date = models.DateField()
    payment_by = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    class Meta:
        ordering = ['payment_date']    
    
    def __str__(self):
        return "Date of payment: "+ str(self.payment_date) +" in amount: EUR "+ str(self.payment_amount) +" .-"
