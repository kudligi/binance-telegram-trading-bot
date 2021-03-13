from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST, require_GET
from rest_framework import status
import os, json    
from decimal import *


from rq import Queue
from worker import conn


from oms import binance_util as Butil
from oms.models import LimitOrder 
from telegram.util import notify_all_in_the_know


# Create your views here.
@require_POST
def alert(request):
    alert = json.loads(request.body)
    print("got an alert ", alert)
    order = {
        'price' : Decimal(alert["price"]).quantize(Decimal('.0001'), rounding=ROUND_DOWN),
        'qty' : Decimal('0.00015'),
        'symbol' : alert['ticker'],
        'side' : alert['action']
    }
    
    response = Butil.place_order(req)
    q = Queue(connection=conn)
    q.enqueue(notify_all_in_the_know, json.dumps(response, indent=True))
    return HttpResponse("ok")
    

@require_GET
def ping(request):
    return HttpResponse("pong")