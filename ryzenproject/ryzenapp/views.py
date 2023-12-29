from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Data
from .serializers import DataSerializers
from rest_framework.renderers import JSONRenderer
# Create your views here.

class Datalist(APIView):
    def get(self,request):
        Data1=Data.objects.all()
        serializer=DataSerializers(Data1,many=True)
        return Response(serializer.data)
        # json_data=JSONRenderer().render(serializer.data)
        # return Response(json_data)
    # this above method is teh another rendering directly from the json renderer of rest
    # which actually renders all the data in the single line and which can be seen in a single
    # line
    # for that i have to import the json renderer for that to work
def homepage(request):
    return HttpResponse("Welcome , for datas  go to -> /Datas end point")