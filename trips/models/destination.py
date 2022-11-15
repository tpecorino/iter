from django.db import models
from .trip import Trip


# Destination model

class Destination(models.Model):
    name = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    arrive_date = models.DateField(blank=True)
    depart_date = models.DateField(blank=True)
    trip = models.ForeignKey(Trip, related_name='destinations', on_delete=models.CASCADE, null=True)

    def _str_(self):
        return self.name
