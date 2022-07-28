from django.contrib import admin
from .models import Trip


class TripAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date')


# Register your models here.

admin.site.register(Trip, TripAdmin)
