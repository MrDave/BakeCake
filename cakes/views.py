from django.shortcuts import render
from django.db import transaction
from cakes.serializers import OrderSerializer
from cakes.models import Cake, Order
from cakes.models import Level, Form, Topping, Berry, Decoration
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse


def show_main(request):
    levels = Level.objects.all()
    forms = Form.objects.all()
    toppings = Topping.objects.all()
    berries = Berry.objects.all()
    decorations = Decoration.objects.all()

    context = {
        "levels": levels,
        "forms": forms,
        "toppings": toppings,
        "berries": berries,
        "decorations": decorations,
    }
    return render(request, "index.html", context=context)


def form_data(request):
    levels = Level.objects.all()
    forms = Form.objects.all()
    toppings = Topping.objects.all()
    berries = Berry.objects.all()
    decorations = Decoration.objects.all()

    response = {
        "Levels": ["не выбрано"] + [level.amount for level in levels],
        "Forms": ["не выбрано"] + [form.name for form in forms],
        "Toppings": ["не выбрано"] + [topping.name for topping in toppings],
        "Berries": ["не выбрано"] + [berry.name for berry in berries],
        "Decors": ["не выбрано"] + [decoration.name for decoration in decorations],
    }

    return JsonResponse(response, json_dumps_params={"ensure_ascii": False})


def form_costs(request):
    levels = Level.objects.all()
    forms = Form.objects.all()
    toppings = Topping.objects.all()
    berries = Berry.objects.all()
    decorations = Decoration.objects.all()

    response = {
        "Levels": [0] + [level.price for level in levels],
        "Forms": [0] + [form.price for form in forms],
        "Toppings": [0] + [topping.price for topping in toppings],
        "Berries": [0] + [berry.price for berry in berries],
        "Decors": [0] + [decoration.price for decoration in decorations],
        "Words": 500
    }

    return JsonResponse(response, json_dumps_params={"ensure_ascii": False})


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
