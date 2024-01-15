from django.db import models
# from .serializers import DataSerializers
# Create your models here.

class Data(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    roll_number=models.IntegerField()

    def __str__(self):
        return self.first_name


