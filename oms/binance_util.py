from binance.client import Client
import os
from decimal import Decimal
from .models import LimitOrder 

def get_client():
    api_key = os.environ.get('BINANCE_API_KEY')
    api_secret = os.environ.get('BINANCE_SECRET_KEY')
    
    if api_key == None or api_secret == None:
        raise Exception("Binance credentials missing")
    
    return Client(api_key, api_secret)

def place_limit_order(f, symbol, price, qty):
    return f(symbol=symbol, price=price, quantity=qty)

def place_order(order):
    client = get_client()
    f = client.order_limit_buy if order["side"] == "buy" else client.order_limit_sell
    symbol = order["symbol"]
    price = order["price"]
    qty = order["qty"]
    response =  place_limit_order(f, symbol, price, qty)
    
    if response["status"] == "NEW" and response["orderId"] != None:
        limit_order = LimitOrder(
            order_id = response["orderId"],
            clientOrderId = response["clientOrderId"],
            price = Decimal(response["price"]),
            quantity = response["origQty"],
            symbol = response["symbol"],
            side = response["side"]
        )
        limit_order.save()
    
    return response



def get_open_orders(symbol):
    client = get_client()
    orders = client.get_open_orders(symbol=symbol)
    return orders

def cancel_order(symbol, orderId):
    client = get_client()
    cancel_receipt = client.cancel_order(symbol=symbol, orderId=orderId)
    return cancel_receipt

def account_info():
    client = get_client()
    res = {}
    # res["history"] = client.get_asset_dividend_history()
    res["info "] = client.get_account()
    res["sub-accounts"] = client.get_sub_account_list()
    return res

