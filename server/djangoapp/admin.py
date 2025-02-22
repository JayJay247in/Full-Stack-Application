from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.

@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Display these fields in the list view
    search_fields = ('name',)  # Enable search by name
    # Add more customization here as needed

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('car_make', 'name', 'type', 'year', 'dealer_id')
    list_filter = ('car_make', 'type', 'year')  # Add filters
    search_fields = ('name', 'car_make__name')  # Search by model name and car make name
    # Add more customization here as needed
