from django.shortcuts import render
from rest_framework import viewsets
from .models import Payment_user , Expired_payments
from .serializers import Payment_userSerializer , Expired_paymentsSerializer
from rest_framework.response import Response
from rest_framework import status
from .pagination import Pagination_payments
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class Rest_Payment(viewsets.ModelViewSet):
  queryset = Payment_user.objects.all()
  serializer_class = Payment_userSerializer
  pagination_class = Pagination_payments
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['payment_date', 'expiration_date']
  throttle_scope = 'pm_app'


  def create(self, request):
    serializer = Payment_userSerializer(data = request.data)

    if serializer.is_valid():
      serializer.save()

      payment_date = serializer.data.get('payment_date')
      expiration_date = serializer.data.get('expiration_date')
      if expiration_date < payment_date:
        record = {
          'penalty_fee_amount': 0.2*float(serializer.data.get('amount')),
          'payment_user_id': serializer.data.get('id'),
          'amount': serializer.data.get('amount'),
          'service_id': serializer.data.get('service_id'),
          'user_id': serializer.data.get('user_id'),
        }
        serializer2 = Expired_paymentsSerializer(data=record)
        if serializer2.is_valid():
          serializer2.save()
          return Response ({
            "ok": True,
            "message":"Record added",
            "data1" : serializer.data,
            "message": "Record added also in Expired Payments",
            "data2": serializer2.data
          } , status = status.HTTP_201_CREATED)

      return Response ({
        "ok": True,
        "message":"Record created",
        "data" : serializer.data,
      }, status = status.HTTP_201_CREATED)
        
    return Response ({
        "ok": False,
        "message":serializer.errors,
      }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)



class Rest_Expired_payments(viewsets.ModelViewSet):
  queryset = Expired_payments.objects.all()
  serializer_class = Expired_paymentsSerializer
  #throttle_scope = 'exp_app'

  # def get_permissions(self):
  #   if self.request.method == 'GET':
  #     return [IsAuthenticated()]
  #   elif self.request.method == 'POST':
  #     return [IsAuthenticated()]

  #   return [IsAdminUser()]