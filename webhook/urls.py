from django.urls import path

from . import views

urlpatterns = [
    path('webhook/', views.alert, "webhook"),
    path('ping/', views.ping, name='ping')
]