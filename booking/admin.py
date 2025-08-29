
from django.contrib import admin
from.models import Register ,TravelOption
from .models import Booking
# Register your models here.

admin.site.register(Register)

@admin.register(TravelOption)
class TravelOptionAdmin(admin.ModelAdmin):
    list_display = ['travel_id', 'travel_type', 'source', 'destination', 'date_time', 'price', 'available_seats']
    list_filter = ['travel_type', 'source', 'destination']
    search_fields = ['source', 'destination']


# @admin.register(Booking)
# class BookingAdmin(admin.ModelAdmin):
#     list_display = ['name', 'travel_option', 'seats_booked', 'booking_time']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['booking_id', 'user', 'travel_option', 'number_of_seats', 'total_price', 'status', 'booking_date']

      