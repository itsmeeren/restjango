import io
import json

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Data
from .serializers import DataSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


def my_view(request):
    # Your view logic here
    return HttpResponse("This view is exempt from CSRF protection.")


class Datalist(APIView):
    def get(self,request):
        Data1=Data.objects.all()
        serializer=DataSerializers(Data1,many=True)
        return Response(serializer.data)
        # json_data=JSONRenderer().render(serializer.data)
        # return HttpResponse(json_data,content_type='application/json')
#     # this above method is the another rendering directly from the json renderer of rest
#     # which actually renders all the data in the single line and which can be seen in a single
#     # line
#     # for that i have to import the json renderer for that to work



# if i want to access one of the raw datass of the json i can give the paramter of id to the views
# of my fucntion and by giving the id parameter in url endpoint i can access





def name_detail(request,x):# x is used as id of the data user wants to get
    Data1 = Data.objects.get(id=x)
    serializer = DataSerializers(Data1)
    # return Response(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
def homepage(request):
    return HttpResponse("Welcome , \n/Datas -> all data\n"
                        "\nDatas/no -> for perticular data")








# This method is used to add the data from the client to the data base
@csrf_exempt# csrf token is exempted beacuse it dont have html to access the csrf token

def data_create(request):
    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=DataSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            # message={"res":"saved!"}
            # json_data=JSONRenderer().render(message)
            return HttpResponse(json_data,content_type="application/json")
        return HttpResponse(json_data, content_type="application/json")



# for giving the data for the clint using id function

def give_data(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id=python_data.get('id',None)
        if id is not None:
            stu=Data.objects.get(id=id)
            serializer=DataSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type="application/json")
    stu=Data.objects.all()
    serializer=DataSerializer(stu,many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type="application/json")











