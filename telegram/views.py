from django.shortcuts import render
from django.views.decorators.http import require_POST
import requests
from .cred import BOT_SEND_URL

from django.http import HttpResponse
import json

# Create your views here.
@require_POST
def talkin_to_me_bruh(request):
    # please insert magic here
    msg = json.loads(request.body)
    id = msg['message']['chat']['id']
    fname = msg['message']["chat"]["first_name"]
    message_text = msg['message']['text']

    json_data = {
        "chat_id" : id,
        "text"  : "Wanna fight {}".format(fname)
    }
    requests.post(BOT_SEND_URL, json=json_data)
    json_data["text"] = "imma whoop your ass!"
    requests.post(BOT_SEND_URL, json=json_data)
    print("Telegram request was ", msg)
    return HttpResponse('OK')


    
