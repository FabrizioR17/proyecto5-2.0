"""project5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , re_path

from pagos.views import Rest_Expired_payments , Rest_Payment
from servicios.views import Rest_services
from usuarios.views import UserCreateView, UserListView
from rest_framework import routers , permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView


schema_view = get_schema_view(
   openapi.Info(
      title="API-PAGOS",
      default_version='v1',
      description="Proyecto5 de sillabuz app de pagos",
      terms_of_service="https://github.com/FabrizioR17",
      contact=openapi.Contact(email="fabriziora12@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'services', Rest_services , 'services')
router.register(r'payment', Rest_Payment , 'payment')
router.register(r'expired-payments', Rest_Expired_payments , 'expired-payments')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/create',  UserCreateView.as_view() , name='users-create'),
    path('users/list',  UserListView.as_view() , name='users-list'),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path("token/", TokenObtainPairView.as_view(), name="get_token"),
    path("token/refresh", TokenRefreshView.as_view(), name="refresh_token"),
    ]

urlpatterns += router.urls
