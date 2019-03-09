from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
#from models import TodoItem
# Create your views here.

from django.http import HttpResponse, JsonResponse

@csrf_exempt
def index(request):
    if(request.method == "GET"):
        return HttpResponse("Hello, world. You're at the todo index.")
    
    if(request.method == "POST"):
         return HttpResponse("POST")

    if(request.method == "DELETE"):
        return HttpResponse("DELETE")