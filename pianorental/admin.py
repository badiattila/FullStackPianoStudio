from django.contrib import admin
from .models import PianosForRent, Payment

# Register the PianosForRent class using the decorator and define list of fields to be displayed on admin
@admin.register(PianosForRent) 
class PianosForRent(admin.ModelAdmin):
    list_display = ('brand', 'price', 'age', 'description', 'status' , 'image', 'at_user', 'rented_since')
    
@admin.register(Payment) 
class Payment(admin.ModelAdmin):
    list_display = ('payment_amount', 'payment_date', 'payment_by')
