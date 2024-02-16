from django.contrib import admin
from cakes.models import Cake, Order
from cakes.models import Level, Shape, Topping, Berry, Decoration


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "levels",
        "shape",
        "topping",
        # "berries_list",
        # "decorations",
        "text",
        "cost"
    ]

    # @admin.display()
    # def berries_list(self, obj):
    #     return obj.berries.values_list("name", flat=True)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "cake",
        "address",
        "delivery_date",
        "delivery_time",
        "cost"
    ]


admin.site.register(Level)
admin.site.register(Shape)
admin.site.register(Topping)
admin.site.register(Berry)
admin.site.register(Decoration)
