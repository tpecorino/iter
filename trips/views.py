from rest_framework import generics
from .models import Trip, Destination, Site, Transportation, Accommodation
from .serializers import TripSerializer, DestinationSerializer, SiteSerializer, TransportationSerializer, \
    AccommodationSerializer


# Trip Views

class TripList(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


# Destination Views

class DestinationList(generics.ListCreateAPIView):
    serializer_class = DestinationSerializer
    lookup_url_kwarg = 'trip_id'

    def get_queryset(self):
        trip_id = self.kwargs.get(self.lookup_url_kwarg)
        destinations = Destination.objects.filter(trip__id=trip_id)
        return destinations


class DestinationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


# Site Views

class SiteList(generics.ListCreateAPIView):
    serializer_class = SiteSerializer
    trip_id_kwarg = 'trip_id'
    destination_id_kwarg = 'destination_id'

    def get_queryset(self):
        trip_id = self.kwargs.get(self.trip_id_kwarg)
        destination_id = self.kwargs.get(self.destination_id_kwarg)

        sites = Site.objects.filter(destination__trip__id=trip_id, destination__id=destination_id)
        return sites


class SiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


# Transportation Views

class TransportationList(generics.ListCreateAPIView):
    serializer_class = TransportationSerializer
    trip_id_kwarg = 'trip_id'
    destination_id_kwarg = 'destination_id'

    def get_queryset(self):
        trip_id = self.kwargs.get(self.trip_id_kwarg)
        destination_id = self.kwargs.get(self.destination_id_kwarg)

        transportation = Transportation.objects.filter(destination__trip__id=trip_id, destination__id=destination_id)
        return transportation


class TransportationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transportation.objects.all()
    serializer_class = TransportationSerializer


# Accommodation Views

class AccommodationList(generics.ListCreateAPIView):
    serializer_class = AccommodationSerializer
    trip_id_kwarg = 'trip_id'
    destination_id_kwarg = 'destination_id'

    def get_queryset(self):
        trip_id = self.kwargs.get(self.trip_id_kwarg)
        destination_id = self.kwargs.get(self.destination_id_kwarg)

        accommodations = Accommodation.objects.filter(destination__trip__id=trip_id, destination__id=destination_id)
        return accommodations


class AccommodationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer
