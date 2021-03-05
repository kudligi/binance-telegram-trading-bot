from django.shortcuts import render
from django.views.decorators.http import require_POST

from django.http import HttpResponse
 
def talkin_to_me_bruh(request):
    # please insert magic here
    return HttpResponse('OK')

# Create your views here.
@require_POST

    
