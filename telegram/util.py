import requests
import os 
from .models import User
from .responses import *
from random import choice

bot_url = os.environ.get('BOT_SEND_URL')
telegram_pwd = os.environ.get('TELEGRAM_PASSWORD')

def send_message(id, text):
    data = {
        "chat_id": id,
        "text": text
    }
    requests.post(bot_url, json=data)

def notify_all_in_the_know(msg):
    users = User.objects.all().filter(knows=True)
    for user in users:
        send_message(user.chat_id, msg)
        print()

def handle_incoming_message(id, name, text):
    text = text.lower()
    if text == telegram_pwd:
        handle_pwd(id, name)

    else:
        respond(id,name)

def handle_pwd(id, name):
    try: 
        user = User.objects.get(chat_id=id)
        user.knows = True
        user.save()
    except (User.DoesNotExist):
        user = User(chat_id=id, username = name, knows= True)
        user.save()
    message = choice(PASS).substitute(name=name)
    send_message(id, message)

def respond(id, name):
    try: 
        user = User.objects.get(chat_id=id)
        message = choice(RANDOM)
        send_message(id, message)
    except (User.DoesNotExist):
        user = User(chat_id=id, username = name, knows= False)
        user.save()
        message = choice(FIGHT)
        send_message(id, message)