from rest_framework import serializers
from .models import Trip, Destination, Accommodation, Transport, Site


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['name', 'description', 'start_date', 'end_date', 'is_active', 'destinations', 'transport']
        depth = 1


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['name', 'country', 'arrive_date', 'depart_date', 'sites', 'accommodations']


class AccommodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accommodation
        fields = ['name', 'check_in_date', 'check_out_date', 'address_link', 'reservation_link']


class TransportSerializer(serializers.Serializer):
    depart = serializers.DateTimeField()
    arrive = serializers.DateTimeField()
    type = serializers.ChoiceField(choices=Transport.TRAVEL_TYPE, default=Transport.DEFAULT)
    info_link = serializers.URLField()


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['name', 'address_link', 'address_resources']
