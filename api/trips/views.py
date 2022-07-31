from rest_framework import viewsets
from .serializers import TripSerializer
from .models import Trip


# Create your views here.

class TripView(viewsets.ModelViewSet):
    serializer_class = TripSerializer
    queryset = Trip.objects.all()
