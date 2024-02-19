from rest_framework import serializers
from cakes.models import Cake, Order
from cakes.models import Level, Form, Topping, Berry, Decoration
from django.contrib.auth.models import User


# class CakeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cake
#         fields = [
#             # "id",
#             "levels",
#             "form",
#             "topping",
#             "berries",
#             "decorations",
#             "text",
#             "cost"
#         ]


class OrderSerializer(serializers.Serializer):
    levels = serializers.PrimaryKeyRelatedField(label='Количество уровней', queryset=Level.objects.all())
    form = serializers.PrimaryKeyRelatedField(label='Форма торта', queryset=Form.objects.all())
    topping = serializers.PrimaryKeyRelatedField(label='Топпинг', queryset=Topping.objects.all())
    berries = serializers.PrimaryKeyRelatedField(label='Ягоды', many=False, queryset=Berry.objects.all(),
                                                 required=False)
    decor = serializers.PrimaryKeyRelatedField(label='Украшения', many=False, queryset=Decoration.objects.all(),
                                               required=False)
    words = serializers.CharField(allow_blank=True, label='Надпись', max_length=75, required=False)
    user = serializers.PrimaryKeyRelatedField(label='Пользователь', read_only=True)
    address = serializers.CharField(label='Адрес', style={'base_template': 'textarea.html'})
    date = serializers.DateField(label='Дата доставки')
    time = serializers.TimeField(label='Время доставки')
    cost = serializers.DecimalField(decimal_places=2, label='Стоимость заказа', max_digits=7, min_value=0,
                                    read_only=True)
