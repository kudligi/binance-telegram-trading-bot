from django.shortcuts import render
from django.views.decorators.http import require_POST

from django.http import HttpResponse
import json

# Create your views here.
def talkin_to_me_bruh(request):
    # please insert magic here
    req = json.loads(request.body)
    print("Telegram request was ", req)
    return HttpResponse('OK')


    
