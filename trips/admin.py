from django.contrib import admin
from .models import Trip, Transportation, Destination, Accommodation, Site


class TripAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'start_date', 'end_date', 'is_active')


class DestinationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'arrive_date', 'depart_date', 'trip_id')


class AccommodationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'check_in_date', 'check_out_date', 'address_link', 'reservation_link', 'destination_id')


class TransportationAdmin(admin.ModelAdmin):
    list_display = ('id', 'depart_time', 'arrive_time', 'start_location', 'end_location', 'type', 'info_link',
                    'destination_id')


class SiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address_link', 'additional_resources', 'destination_id')


# Register your models here.

admin.site.register(Trip, TripAdmin)
admin.site.register(Destination, DestinationAdmin)
admin.site.register(Accommodation, AccommodationAdmin)
admin.site.register(Transportation, TransportationAdmin)
admin.site.register(Site, SiteAdmin)
