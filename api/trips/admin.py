from django.contrib import admin
from .models import Trip, Transport, Destination, Accommodation, Site


class TripAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date', 'is_active', 'transport')


class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'arrive_date', 'depart_date')


class AccommodationAdmin(admin.ModelAdmin):
    list_display = ('name', 'check_in_date', 'check_out_date', 'address_link', 'reservation_link')


class TransportAdmin(admin.ModelAdmin):
    list_display = ('depart', 'arrive', 'type', 'arrive', 'origin', 'destination')


class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'address_link', 'additional_resources')


# Register your models here.

admin.site.register(Trip, TripAdmin)
admin.site.register(Destination, DestinationAdmin)
admin.site.register(Accommodation, AccommodationAdmin)
admin.site.register(Transport, TransportAdmin)
admin.site.register(Site, SiteAdmin)
