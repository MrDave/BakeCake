from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Level(models.Model):
    amount = models.IntegerField(verbose_name="количество уровней")
    price = models.IntegerField(verbose_name="стоимость", validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = "уровень"
        verbose_name_plural = "уровни"

    def __str__(self):
        return str(self.amount)


class Form(models.Model):
    name = models.CharField(verbose_name="название", max_length=20)
    price = models.IntegerField(verbose_name="стоимость", validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = "форма"
        verbose_name_plural = "формы"

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(verbose_name="название", max_length=20)
    price = models.IntegerField(verbose_name="стоимость", validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = "топпинг"
        verbose_name_plural = "топпинги"

    def __str__(self):
        return self.name


class Berry(models.Model):
    name = models.CharField(verbose_name="название", max_length=20)
    price = models.IntegerField(verbose_name="стоимость", validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = "ягода"
        verbose_name_plural = "ягоды"

    def __str__(self):
        return self.name


class Decoration(models.Model):
    name = models.CharField(verbose_name="название", max_length=20)
    price = models.IntegerField(verbose_name="стоимость", validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = "украшение"
        verbose_name_plural = "украшения"

    def __str__(self):
        return self.name


class CakeQuerySet(models.QuerySet):
    def fetch_with_base_price(self):
        return self.annotate(
            total_price=models.Sum(
                (
                        models.F("levels__price") +
                        models.F("form__price") +
                        models.F("topping__price")
                ),
                output_field=models.IntegerField()
            )
        )


class Cake(models.Model):
    levels = models.ForeignKey(
        Level,
        verbose_name="количество уровней",
        on_delete=models.PROTECT,
        related_name="cakes"
    )
    form = models.ForeignKey(
        Form,
        verbose_name="форма торта",
        on_delete=models.PROTECT,
        related_name="cakes"
    )
    topping = models.ForeignKey(
        Topping,
        verbose_name="топпинг",
        on_delete=models.PROTECT,
        related_name="cakes"
    )
    berries = models.ForeignKey(
        Berry,
        verbose_name="ягоды",
        related_name="cakes",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    decorations = models.ForeignKey(
        Decoration,
        verbose_name="украшения",
        related_name="cakes",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    text = models.CharField(
        verbose_name="надпись",
        max_length=75,
        blank=True
    )
    objects = CakeQuerySet.as_manager()

    class Meta:
        verbose_name = "торт"
        verbose_name_plural = "торты"

    def __str__(self):
        return f"{self.levels}-слойный {self.form}, топпинг - {self.topping}"


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name="пользователь", on_delete=models.CASCADE, related_name="orders")
    cake = models.ForeignKey(Cake, verbose_name="торт", on_delete=models.CASCADE, related_name="orders")
    address = models.TextField(verbose_name="адрес", editable=True)
    order_notes = models.TextField(verbose_name="примечание к заказу", blank=True)
    delivery_notes = models.TextField(verbose_name="примечание для курьера", blank=True)
    delivery_date = models.DateField(verbose_name="дата доставки")
    delivery_time = models.TimeField(verbose_name="время доставки")
    cost = models.DecimalField(
        verbose_name="стоимость заказа",
        validators=[MinValueValidator(0)],
        decimal_places=2,
        max_digits=7
    )

    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "заказы"

    def __str__(self):
        return f"{self.cake} - {self.address}"
