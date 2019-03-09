from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

# Create your views here.

from django.http import HttpResponse

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
    
    