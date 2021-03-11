from django.urls import path

from . import views

urlpatterns = [
    path('order/place/', views.place_order, name="place limit order"),
    path('order/get_open/exchange/<str:symbol>/', views.get_open_orders, name="get open orders from exchange"),
    path('order/get_all/db/', views.get_all_orders_db, name="get open orders from exchange"),
    path('order/cancel/', views.cancel_order, name="cancel order"),
    path('account/', views.get_account_info, name = "account info"),
]