from rest_framework import serializers
from .models import Trip, Destination, Accommodation, Transportation, Site


class AccommodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accommodation
        fields = ['id', 'name', 'check_in_date', 'check_out_date', 'address_link', 'reservation_link']


class TransportationSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=Transportation.TRAVEL_TYPE, default=Transportation.DEFAULT)

    class Meta:
        model = Transportation
        fields = ['id', 'depart_time', 'arrive_time', 'start_location', 'end_location', 'info_link', 'type']


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['id', 'name', 'address_link', 'time', 'additional_resources']


class DestinationSerializer(serializers.ModelSerializer):
    sites = SiteSerializer(many=True, required=False)
    accommodations = AccommodationSerializer(many=True, required=False)
    transportation = TransportationSerializer(many=True, required=False)

    class Meta:
        model = Destination
        fields = ['id', 'name', 'country', 'arrive_date', 'depart_date', 'transportation', 'accommodations', 'sites']


class TripSerializer(serializers.ModelSerializer):
    destinations = DestinationSerializer(many=True, required=False)

    class Meta:
        model = Trip
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'is_active', 'destinations']
        depth = 1
