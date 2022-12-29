from rest_framework import serializers
from .models import Payment_user , Expired_payments

class Payment_userSerializer(serializers.ModelSerializer):
  class Meta:
    model = Payment_user
    fields = '__all__'

  def validate(self,data):
    amount = data.get('amount')
    if amount < 0:
      raise serializers.ValidationError('Monto no puede ser negativo')
    return data

class Expired_paymentsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Expired_payments
    fields = '__all__'