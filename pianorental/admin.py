from django.contrib import admin
from .models import PianosForRent

# Register the PianosForRent class using the decorator and define list of fields to be displayed on admin
@admin.register(PianosForRent) 
class PianosForRent(admin.ModelAdmin):
    list_display = ('brand', 'price', 'age', 'description', 'status' , 'image', 'at_user', 'rented_since')
    
