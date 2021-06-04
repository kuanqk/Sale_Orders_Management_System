from rest_framework.decorators import api_view
from django.shortcuts import HttpResponse
from rest_framework import status
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
from sales.app.models import Order
import json
import datetime, pytz


def serialize_order(order):
    serialized = model_to_dict(order)
    serialized["date"] = str(order.date)
    serialized["amount"] = float(order.amount)
    serialized["price"] = float(order.price)
    serialized["quantity"] = float(order.quantity)
    return serialized


@api_view(['GET', 'POST'])
def orders(request):
    if request.user.is_anonymous:
        return HttpResponse(json.dumps({"detail": "Not authorized"}), status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "POST":
        order = Order()
        order.date = request.data.get("date", "")
        order.item = request.data.get("item", "")
        order.price = float(request.data.get("price", ""))
        order.quantity = float(request.data.get("quantity", ""))
        order.amount = float(request.data.get("amount", ""))  # <- this line is not correct
        order.save()
        return HttpResponse(json.dumps({"data": serialize_order(order)}), status=status.HTTP_201_CREATED)

    # PUT YOUR METHODS HERE FOR GET method of ALL ITEMS

    return HttpResponse(json.dumps({"detail": "Wrong method"}), status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(['GET', 'PUT', 'DELETE'])
def order(request, order_id):
    if request.user.is_anonymous:
        return HttpResponse(json.dumps({"detail": "Not authorized"}), status=status.HTTP_401_UNAUTHORIZED)

    try:
        order = Order.objects.get(pk=order_id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({"detail": "Not found"}), status=status.HTTP_404_NOT_FOUND)

    # PUT YOUR METHODS HERE FOR GET, PUT and DELETE of INDIVIDUAL ITEMS

    return HttpResponse(json.dumps({"detail": "Wrong method"}), status=status.HTTP_501_NOT_IMPLEMENTED)