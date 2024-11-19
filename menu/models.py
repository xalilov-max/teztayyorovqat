from django.db import models

class FoodCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")
    description = models.TextField(null=True, blank=True, verbose_name="Kategoriya haqida")

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ovqat nomi")
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name='foods')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    is_available = models.BooleanField(default=True, verbose_name="Mavjudmi?")

    def __str__(self):
        return self.name


class Order(models.Model):
    food = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField(verbose_name="Soni")
    ordered_at = models.DateTimeField(auto_now_add=True, verbose_name="Buyurtma vaqti")

    def __str__(self):
        return f"Order of {self.food.name} (x{self.quantity})"
