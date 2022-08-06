from django.db import models


# Trip model

class Trip(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=255)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    is_active = models.BooleanField(default=False)

    def _str_(self):
        return self.name
