from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth.models import User
# Create your views here.

class UserCreateView(generics.CreateAPIView):
  serializer_class = UserSerializer

class UserListView(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer