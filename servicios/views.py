from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ServicesSerializer
from .models import Services
# Create your views here.

class Rest_services(viewsets.ModelViewSet):
  queryset = Services.objects.all()
  serializer_class = ServicesSerializer
  #throttle_classes = 'all'