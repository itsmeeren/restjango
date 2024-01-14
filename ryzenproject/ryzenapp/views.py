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
        # return HttpResponse(json_data,content_type='application/json')
#     # this above method is teh another rendering directly from the json renderer of rest
#     # which actually renders all the data in the single line and which can be seen in a single
#     # line
#     # for that i have to import the json renderer for that to work



# if i want to access one of the raw datass of the json i can give the paramter of id to the views
# of my fucntion and by giving the id parameter in url endpoint i can access





def name_detail(request,x):
    Data1 = Data.objects.get(id=x)
    serializer = DataSerializers(Data1)
    # return Response(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
def homepage(request):
    return HttpResponse("Welcome , \n/Datas -> all data\n"
                        "\nDatas/no -> for perticular data")