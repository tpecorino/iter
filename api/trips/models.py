from django.db import models


# Create your models here.

class Trip(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def _str_(self):
        return self.name
