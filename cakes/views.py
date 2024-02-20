import datetime

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from rest_framework.decorators import api_view

from cakes.models import Cake, Order
from cakes.models import Level, Form, Topping, Berry, Decoration
from cakes.serializers import OrderSerializer


def show_main(request):
    levels = Level.objects.all()
    forms = Form.objects.all()
    toppings = Topping.objects.all()
    berries = Berry.objects.all()
    decorations = Decoration.objects.all()

    user = request.user

    context = {
        "levels": levels,
        "forms": forms,
        "toppings": toppings,
        "berries": berries,
        "decorations": decorations,
        "user": user,
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


@login_required
def profile(request):
    if request.user.is_authenticated:
        user = request.user

    orders = Order.objects.filter(user=user).order_by("-id")
    context = {
        "user": user,
        "user_phone": user.phonenumber_set.first(),
        "orders": orders
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
        "berries",
        "decor",
        "words"
    ]
    cake_payload = {key: serializer.validated_data.pop(key, None) for key in cake_keys}

    cake_payload["decorations"] = cake_payload.pop("decor")
    text = cake_payload.pop("words")

    cake = Cake.objects.create(text=text, **cake_payload)

    base_cake_price = Cake.objects.filter(id=cake.id).fetch_with_base_price().first().total_price
    words_price = 500 if cake.text else 0
    berries_price = cake.berries.price if cake.berries else 0
    decorations_price = cake.decorations.price if cake.decorations else 0

    delivery_date = serializer.validated_data.pop("date")
    delivery_time = serializer.validated_data.pop("time")
    order_notes = serializer.validated_data.pop("comments", "")
    delivery_notes = serializer.validated_data.pop("delivcomments", "")

    quick_delivery_markup = 1.2 if (datetime.datetime.combine(delivery_date, delivery_time) -
                                    datetime.datetime.now() < datetime.timedelta(days=1)) else 1

    order_cost = (base_cake_price + words_price + berries_price + decorations_price) * quick_delivery_markup
    order = Order.objects.create(
        user=user,
        cake=cake,
        cost=order_cost,
        delivery_date=delivery_date,
        delivery_time=delivery_time,
        order_notes=order_notes,
        delivery_notes=delivery_notes,
        **serializer.validated_data
    )

    return redirect("profile")
