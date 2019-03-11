from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import HttpResponse
from rest_framework import generics
from .models import todo
from .serializers import todoSerializer

# Create your views here.

class ListTodosView(generics.ListAPIView):
    #Provides a method handler
    queryset = todo.objects.all()
    serializer_class = todoSerializer 

@csrf_exempt
def index(request):
    if(request.method == "GET"):
        body = request.body
        serializedBody = serializers.serialize('json', body)        
        return HttpResponse(serializedBody)
    
    if(request.method == "POST"):
        body = request.body
        return HttpResponse(body)

    if(request.method == "DELETE"):
        return HttpResponse("DELETE")
    
    
