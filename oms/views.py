from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse
from rest_framework import status
import os, json        
from django.core import serializers
from rq import Queue
from worker import conn


from . import validators
from . import binance_util as Butil
from .models import LimitOrder 
from telegram.views import notify_users

# Create your views here.
@require_POST
def place_order(request):
    res = {}
    status_code = status.HTTP_200_OK
    try:
        req = json.loads(request.body.decode("utf-8"))
    except Exception as e:
        res["details"] = "Invalid request body"
    validation = validators.validate_api(req)
    if not validation["success"]:
        res["errors"] = validation["errors"]
        status_code = status.HTTP_400_BAD_REQUEST
    else:
        # req["price"] = str(req["price"])
        res["details"] = "Validation passed"
        res["order_response"] = Butil.place_order(req)
    q = Queue(connection=conn)
    q.enqueue(notify_users, json.dumps(res, indent=True))
    return JsonResponse(res, status=status_code)

@require_GET
def get_open_orders(request, symbol):   
    res = {}
    status_code = status.HTTP_200_OK
    # res["orders"] = symbol
    res["orders"] = Butil.get_open_orders(symbol)
    q = Queue(connection=conn)
    q.enqueue(notify_users, json.dumps(res, indent=True))
    return JsonResponse(res, status=status_code)

@require_GET
def get_account_info(request):   
    res = {}
    status_code = status.HTTP_200_OK
    # res["orders"] = symbol
    res["info"] = Butil.account_info()
    q = Queue(connection=conn)
    q.enqueue(notify_users, json.dumps(res, indent=True))
    return JsonResponse(res, status=status_code)

@require_POST
def cancel_order(request):   
    res = {}
    status_code = status.HTTP_200_OK
    try:
        req = json.loads(request.body.decode("utf-8"))
    except Exception as e:
        res["details"] = "Invalid request body"
    # res["orders"] = symbol
    res["cancel_receipt"] = Butil.cancel_order(req["symbol"], req["orderID"])
    q = Queue(connection=conn)
    q.enqueue(notify_users, json.dumps(res, indent=True))
    return JsonResponse(res, status=status_code)

@require_GET
def get_all_orders_db(request):
    res = {}
    status_code = status.HTTP_200_OK
    try:
        req = json.loads(request.body.decode("utf-8"))
    except Exception as e:
        res["details"] = "Invalid request body"
    orders = LimitOrder.objects.all()
    res["orders"] = json.loads(serializers.serialize('json', orders))
    q = Queue(connection=conn)
    q.enqueue(notify_users, json.dumps(res, indent=True))
    return JsonResponse(res, status=status_code)