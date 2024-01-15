import io

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Data
from .serializers import DataSerializers

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






from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer  # Import JSONRenderer
from .serializers import DataSerializers
import io

@api_view(['POST'])
@csrf_exempt
def data_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        serializer = DataSerializers(data=python_data)

        if serializer.is_valid():
            serializer.save()
            return Response({"res": "saved!"}, content_type="application/json", renderer_classes=[JSONRenderer])
        return Response(serializer.errors, status=400, content_type="application/json", renderer_classes=[JSONRenderer])

    return Response({"res": "Invalid request method"}, status=405, content_type="application/json", renderer_classes=[JSONRenderer])


    return Response({"res": "Invalid request method"}, status=405)
