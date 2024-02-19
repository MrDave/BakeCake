from rest_framework import serializers
from cakes.models import Cake, Order
from cakes.models import Level, Form, Topping, Berry, Decoration
from django.contrib.auth.models import User


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


# class OrderSerializer(serializers.ModelSerializer):
#     # cake = CakeSerializer()
#     levels = serializers.PrimaryKeyRelatedField(label='Количество уровней', queryset=Level.objects.all())
#     form = serializers.PrimaryKeyRelatedField(label='Форма торта', queryset=Form.objects.all())
#     topping = serializers.PrimaryKeyRelatedField(label='Топпинг', queryset=Topping.objects.all())
#     berries = serializers.PrimaryKeyRelatedField(allow_empty=True, label='Ягоды',
#                                                  many=True, queryset=Berry.objects.all())
#     decorations = serializers.PrimaryKeyRelatedField(allow_empty=True, label='Украшения',
#                                                      many=True, queryset=Decoration.objects.all())
#     text = serializers.CharField(allow_blank=True, label='Надпись', max_length=75, required=False)
#     # cost = serializers.DecimalField(decimal_places=2, label='Стоимость', max_digits=7, min_value=0)
#
#     class Meta:
#         model = Order
#         fields = [
#             "user",
#             # "cake",
#             "address",
#             "delivery_date",
#             "delivery_time",
#             # "cost",
#             "levels",
#             "form",
#             "topping",
#             "berries",
#             "decorations",
#             "text",
#         ]
#
#     # def create(self, validated_data):
#     #     cake_keys = ["levels", "form", "topping", "berries", "decorations", "text", "cost"]
#     #     cake_payload = {key: validated_data.pop(key) for key in cake_keys}
#     #     cake = Cake(**cake_payload)
#     #     return Order(cake=cake, **validated_data)

class OrderSerializer(serializers.Serializer):
    levels = serializers.PrimaryKeyRelatedField(label='Количество уровней', queryset=Level.objects.all())
    form = serializers.PrimaryKeyRelatedField(label='Форма торта', queryset=Form.objects.all())
    topping = serializers.PrimaryKeyRelatedField(label='Топпинг', queryset=Topping.objects.all())
    # berries = serializers.PrimaryKeyRelatedField(allow_empty=True, label='Ягоды',
    #                                              many=True, queryset=Berry.objects.all())
    # decor = serializers.PrimaryKeyRelatedField(allow_empty=True, label='Украшения',
    #                                                  many=True, queryset=Decoration.objects.all())
    words = serializers.CharField(allow_blank=True, label='Надпись', max_length=75, required=False)
    user = serializers.PrimaryKeyRelatedField(label='Пользователь', read_only=True)
    address = serializers.CharField(label='Адрес', style={'base_template': 'textarea.html'})
    date = serializers.DateField(label='Дата доставки')
    time = serializers.TimeField(label='Время доставки')
    cost = serializers.DecimalField(decimal_places=2, label='Стоимость заказа', max_digits=7, min_value=0, read_only=True)
