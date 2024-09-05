from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Data.models import *
from .serializers import TasksSerializers




@api_view(['GET'])
def getData(request):
    tasks = Tasks.objects.all()
    serializer = TasksSerializers(tasks,many=True)


    return Response(serializer.data)
    