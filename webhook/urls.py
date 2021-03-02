from django.urls import path

from . import views

urlpatterns = [
    path('webhook/', views.alert, "tw-alert-hook"),
    path('ping/', views.ping, name='ping')
]