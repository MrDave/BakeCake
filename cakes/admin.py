from django.contrib import admin
from cakes.models import Cake, Order
from cakes.models import Level, Form, Topping, Berry, Decoration


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "levels",
        "form",
        "topping",
        # "berries_list",
        # "decorations",
        "text",
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
admin.site.register(Form)
admin.site.register(Topping)
admin.site.register(Berry)
admin.site.register(Decoration)
