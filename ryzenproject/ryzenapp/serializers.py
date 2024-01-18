
# this file is created by me to serialize the data in my model

from rest_framework import serializers
from .models import Data


# class DataSerializers(serializers.ModelSerializer):
#     class Meta:
#         model=Data
#         fields='__all__'
#     def create(self, validated_data):
#         return Data.objects.create(**validated_data)



class DataSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    roll_number = serializers.IntegerField()

    def create(self, validate_data):
        return Data.objects.create(**validate_data)
    def update(self, instance, validated_data):
        instance.first_name=validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.roll_number = validated_data.get('roll_number', instance.roll_number)
        instance.save()
        return instance
    def __delete__(self, instance):


