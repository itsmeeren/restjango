from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Data
from .serializers import DataSerializers
# Create your views here.

class Datalist(APIView):
    def get(self,request):
        Data1=Data.objects.all()
        serializer=DataSerializers(Data1,many=True)
        return Response(serializer.data)
def homepage(request):
    return HttpResponse("Welcome , for datas  go to -> /Datas end point")