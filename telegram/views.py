from django.shortcuts import render
from django.views.decorators.http import require_POST
import requests
from .cred import BOT_SEND_URL
from .models import User



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
    handle(id, name, msg)
    print("Telegram request was ", msg)
    return HttpResponse('OK')

def handle(id, name, text):
    msg = text.lower()
    if msg == "iabpw":
        create_user_that_knows(id, name)
    else:
        create_user_that_doesnt(id, name)

def check_user_exists(id):
    try:
        user = User.objects.get(chat_id=id)
        return True
    except (User.DoesNotExist):
        return False

def create_user_that_knows(id, name):
    if (not check_user_exists(id)):
        user = new User(chat_id=id, username = "name", knows= True)
    send_message(id, "youre cool")

def create_user_that_doesnt(id, name):
    if (not check_user_exists(id)):
        user = new User(chat_id=id, username = "name", knows= False)
        send_message(id, "Sorry I dint want to talk to you!")
    else:
        send_message(id, "wanna fight {}?".format(name))
        send_message(id, "Imma whoop your ass!!")

def send_message(id, text):
    data = {
        "id": id,
        "text": test 
    }
    requests.post(BOT_SEND_URL, json=data)
        

    
    
