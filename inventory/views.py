from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Vehicle,Booking
from .serializers import VehicleSerializer,BookingSerializer

# Create your views here.

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.select_related("vehicle").all()
    serializer_class = BookingSerializer



