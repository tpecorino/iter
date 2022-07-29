from django.contrib import admin
from .models import Trip, Transport


class TripAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date', 'is_active', 'transport')


class TransportAdmin(admin.ModelAdmin):
    list_display = ('depart', 'arrive', 'type')


# Register your models here.

admin.site.register(Trip, TripAdmin)
admin.site.register(Transport, TransportAdmin)
