from django.db import models
from .transport import Transport


# Trip model.

class Trip(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=255)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    is_active = models.BooleanField(null=True)
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE, null=True)

    def _str_(self):
        return self.name