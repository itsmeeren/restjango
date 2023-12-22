
# this file is created by me to serialize the data in my model

from rest_framework import serializers
from .models import Data


class DataSerializers(serializers.ModelSerializer):
    class Meta:
        model=Data
        fields='__all__'



