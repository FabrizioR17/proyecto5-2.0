from django.db import models

# Create your models here.

class Services(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  logo = models.URLField(max_length=255)
  prefijo = models.CharField(max_length=3 , default= '--')

  class Meta:
    db_table = 'services'

  def __str__(self) -> str:
    return self.name