from django.db import models
from .accommodation import Accommodation
from .site import Site


# Destination model

class Destination(models.Model):
    name = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    arrive_date = models.DateField(null=True)
    depart_date = models.DateField(null=True)
    sites = models.ForeignKey(Site, on_delete=models.CASCADE, blank=True, null=True)
    accommodations = models.ForeignKey(Accommodation, on_delete=models.CASCADE, blank=True, null=True)

    def _str_(self):
        return self.name
