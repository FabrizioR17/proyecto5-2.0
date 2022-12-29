from django.db import models

from django.contrib.auth.models import User
from servicios.models import Services

# Create your models here.
class Payment_user(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    expiration_date = models.DateField()

    class Meta:
        db_table = 'payment_user'

class Expired_payments(models.Model):
    payment_user_id = models.ForeignKey(Payment_user, on_delete=models.CASCADE)
    penalty_fee_amount = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE, default=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        db_table = 'expired_payment'