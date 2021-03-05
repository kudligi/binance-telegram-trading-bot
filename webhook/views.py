from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST, require_GET
import json


# Create your views here.
@require_POST
def alert(request):
    alert = json.loads(request.body)
    print("got an alert ", alert)
    return HttpResponse(alert)
    

@require_GET
def ping(request):
    return HttpResponse("pong")