from django.shortcuts import render
from django.views.decorators.http import require_POST
import requests
from .cred import BOT_SEND_URL
from .models import User
from . import util



from django.http import HttpResponse
import json

# Create your views here.
@require_POST
def talkin_to_me_bruh(request):
    # please insert magic here
    msg = json.loads(request.body)
    id = msg['message']['chat']['id']
    name = msg['message']["chat"]["first_name"]
    msg = msg['message']['text']
    util.handle_incoming_message(id, name, msg)
    print("Telegram request was ", msg)
    return HttpResponse('OK')

