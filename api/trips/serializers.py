from rest_framework import serializers
from .models import Trip, Destination, Accommodation, Transportation, Site


class AccommodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accommodation
        fields = ['name', 'check_in_date', 'check_out_date', 'address_link', 'reservation_link']


class TransportationSerializer(serializers.Serializer):
    depart_time = serializers.DateTimeField()
    arrive_time = serializers.DateTimeField()
    start_location = serializers.CharField()
    end_location = serializers.CharField()
    type = serializers.ChoiceField(choices=Transportation.TRAVEL_TYPE, default=Transportation.DEFAULT)
    info_link = serializers.URLField()


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['name', 'address_link', 'additional_resources']


class DestinationSerializer(serializers.ModelSerializer):
    sites = SiteSerializer(many=True, required=False)
    accommodations = AccommodationSerializer(many=True, required=False)
    transportation = TransportationSerializer(many=True, required=False)

    class Meta:
        model = Destination
        fields = ['name', 'country', 'arrive_date', 'depart_date', 'transportation', 'accommodations', 'sites']


class TripSerializer(serializers.ModelSerializer):
    destinations = DestinationSerializer(many=True, required=False)

    class Meta:
        model = Trip
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'is_active', 'destinations']
        depth = 1
