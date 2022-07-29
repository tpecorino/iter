from django.db import models


# Transport model.

class Transport(models.Model):
    DEFAULT = 'DEFAULT'
    TRAVEL_TYPE = [
        ('DEFAULT', ''),
        ('AIR', 'Airplane'),
        ('TRAIN', 'Train'),
        ('BOAT', 'Boat'),
        ('BUS', 'Bus'),
        ('CAR', 'Car')
    ]
    depart = models.DateTimeField(null=True)
    arrive = models.DateTimeField(null=True)
    type = models.CharField(max_length=25, choices=TRAVEL_TYPE, default=DEFAULT)
    info_link = models.URLField(null=True)

    def _str_(self):
        return self.DEFAULT, self.TRAVEL_TYPE
