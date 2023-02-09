import  datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Car(models.Model):
    # class Choice(models.M)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=30)
    version = models.CharField(max_length=50)
    cylinder = models.IntegerField(default=0)
    years = models.IntegerField(default=0)

    #image

    def __str__(self):
        return self.brand, self.model





