from django.contrib import admin
from .models import Pianos

# Register the PianosForRent class using the decorator and define list of fields to be displayed on admin
@admin.register(Pianos) 
class Pianos(admin.ModelAdmin):
    list_display = ('brand', 'price', 'age', 'description', 'image')
