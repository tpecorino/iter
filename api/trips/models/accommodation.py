from django.db import models


# Accommodation model

class Accommodation(models.Model):
    name = models.CharField(max_length=120)
    check_in_date = models.DateTimeField(null=True)
    check_out_date = models.DateTimeField(null=True)
    address_link = models.URLField(blank=True)
    reservation_link = models.URLField(null=True)

    def _str_(self):
        return self.name
