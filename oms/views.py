from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET
import json
from django.http import HttpResponse

# Create your views here.
@require_POST
def place_order(request):
    order = json.loads(request.body)
    return HttpResponse(order)

