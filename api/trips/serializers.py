from rest_framework import serializers
from .models import Transport


class TransportSerializer(serializers.Serializer):
    depart = serializers.DateTimeField()
    arrive = serializers.DateTimeField()
    type = serializers.ChoiceField(choices=Transport.TRAVEL_TYPE, default=Transport.DEFAULT)
    info_link = serializers.URLField()


class TripSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    description = serializers.CharField(max_length=255)
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    is_active = serializers.BooleanField()
    transport = TransportSerializer()
