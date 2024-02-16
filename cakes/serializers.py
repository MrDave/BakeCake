from rest_framework import serializers
from cakes.models import Cake, Order


class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        fields = [
            # "id",
            "levels",
            "form",
            "topping",
            "berries",
            "decorations",
            "text",
            "cost"
        ]


class OrderSerializer(serializers.ModelSerializer):
    cake = CakeSerializer()

    class Meta:
        model = Order
        fields = [
            "user",
            "cake",
            "address",
            "delivery_date",
            "delivery_time",
            "cost"
        ]

    # def create(self, validated_data):
    #     cake_keys = ["levels", "form", "topping", "berries", "decorations", "text", "cost"]
    #     cake_payload = {key: validated_data.pop(key) for key in cake_keys}
    #     cake = Cake(**cake_payload)
    #     return Order(cake=cake, **validated_data)
