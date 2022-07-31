from django.db import models


# Site model

class Site(models.Model):
    name = models.CharField(max_length=120)
    address_link = models.URLField(null=True)
    additional_resources = models.TextField(blank=True, max_length=255)

    def _str_(self):
        return self.name
