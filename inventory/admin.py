from django.contrib import admin
from .models import Vehicle,Booking

# Register your models here.

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("id","name","brand","year","price_per_day","fuel_type","is_available")
    list_filter = ("brand","fuel_type","is_available")

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id","vehicle","customer_name","customer_phone","start_date","end_date","total_amount")
        

