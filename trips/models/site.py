from django.db import models
from .destination import Destination


# Site model

class Site(models.Model):
    name = models.CharField(max_length=120)
    address_link = models.URLField(blank=True)
    additional_resources = models.TextField(blank=True, max_length=255)
    time = models.DateTimeField(blank=True, null=True)
    destination = models.ForeignKey(Destination, related_name='sites', on_delete=models.CASCADE, blank=True,
                                    null=True)

    def _str_(self):
        return self.name
