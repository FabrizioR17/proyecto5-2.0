from django.urls import path
from .views import get_user

urlpatterns = [
  path('get-usuarios/<str:username>/' , get_user , name = "get_user"),
]