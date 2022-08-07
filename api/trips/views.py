from rest_framework import generics
from .models import Trip, Destination, Site
from .serializers import TripSerializer, DestinationSerializer, SiteSerializer


# Create your views here.

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
        print(sites)
        return sites


class SiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
