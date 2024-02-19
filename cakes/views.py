from django.shortcuts import render
from django.db import transaction
from cakes.serializers import OrderSerializer
from cakes.models import Cake, Order
from cakes.models import Level, Form, Topping, Berry, Decoration
from django.contrib.auth.models import User
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


def profile(request):
    user = User.objects.all()

    if request.user.is_authenticated:
        user = request.user

    context = {
        "first_name": user.first_name,
        "last_name": user.first_name,
        "email": user.email,
    }

    return render(request, "lk.html", context=context)


@api_view(["POST"])
@transaction.atomic()
def create_order(request):
    lowercase_payload = {key.lower(): value for key, value in request.data.items()}
    serializer = OrderSerializer(data=lowercase_payload)
    serializer.is_valid(raise_exception=True)

    if request.user.is_authenticated:
        user = request.user

    cake_keys = [
        "levels",
        "form",
        "topping",
        # "berries",
        # "decor",
        "words"
    ]
    cake_payload = {key: serializer.validated_data.pop(key) for key in cake_keys}

    # cake_payload = serializer.validated_data.pop("cake")

    # TODO: установить ягоды и декор в торт
    # berries = cake_payload.pop("berries")
    # decorations = cake_payload.pop("decor")
    text = cake_payload.pop("words")

    cake = Cake.objects.create(text=text, cost=42200, **cake_payload)
    # cake.berries.set(berries)
    # cake.decorations.set(decorations)
    delivery_date = serializer.validated_data.pop("date")
    delivery_time = serializer.validated_data.pop("time")
    # TODO: высчитать реальную стоимость
    order = Order.objects.create(user=user, cake=cake, cost=9999, delivery_date=delivery_date,
                                 delivery_time=delivery_time, **serializer.validated_data)
    return Response(
        {
            "order_id": order.id,
            "user_id": order.user.id,
            "cake": {
                "cake_id": cake.id,
                "levels": cake.levels.amount,
                "form": cake.form.name,
                "topping": cake.topping.name,
                "berries": cake.berries.name,
                "decorations": cake.decorations.name,
                "text": cake.text,
                "cost": cake.cost,
            },
            "address": order.address,
            "notes": order.notes,
            "delivery_date": order.delivery_date,
            "delivery_time": order.delivery_time,
            "cost": order.cost,
        }
    )
