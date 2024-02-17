from django.shortcuts import render
from django.db import transaction
from cakes.serializers import OrderSerializer
from cakes.models import Cake, Order
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
@transaction.atomic()
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # cake_keys = ["levels", "form", "topping", "berries", "decorations", "text", "cost"]
    cake_payload = serializer.validated_data.pop("cake")
    berries = cake_payload.pop("berries")
    decorations = cake_payload.pop("decorations")

    cake = Cake.objects.create(**cake_payload)
    cake.berries.set(berries)
    cake.decorations.set(decorations)

    order = Order.objects.create(cake=cake, **serializer.validated_data)
    return Response(
        OrderSerializer(order).data
    )
