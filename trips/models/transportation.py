from django.db import models
from .destination import Destination


# Transportation model

class Transportation(models.Model):
    DEFAULT = 'DEFAULT'
    TRAVEL_TYPE = [
        ('DEFAULT', ''),
        ('AIR', 'Airplane'),
        ('TRAIN', 'Train'),
        ('BOAT', 'Boat'),
        ('BUS', 'Bus'),
        ('CAR', 'Car')
    ]
    initial_transport = models.BooleanField(default=False)
    depart_time = models.DateTimeField(blank=True)
    arrive_time = models.DateTimeField(blank=True)
    start_location = models.CharField(max_length=120, blank=True)
    end_location = models.CharField(max_length=120, blank=True)
    type = models.CharField(max_length=25, choices=TRAVEL_TYPE, default=DEFAULT)
    info_link = models.URLField(blank=True)
    destination = models.ForeignKey(Destination, related_name='transportation', on_delete=models.CASCADE, blank=True,
                                    null=True)

    class Meta:
        verbose_name_plural = 'Transportation'

    def _str_(self):
        return self.DEFAULT, self.TRAVEL_TYPE
