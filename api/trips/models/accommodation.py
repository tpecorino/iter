from django.db import models
from .destination import Destination


# Accommodation model

class Accommodation(models.Model):
    name = models.CharField(max_length=120)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    address_link = models.URLField(blank=True)
    reservation_link = models.URLField(blank=True)
    destination = models.ForeignKey(Destination, related_name='accommodations', on_delete=models.CASCADE, blank=True,
                                    null=True)

    def _str_(self):
        return self.name
