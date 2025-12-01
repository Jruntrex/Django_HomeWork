from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва")
    instrument_type = models.CharField(max_length=50, verbose_name="Тип інструменту")
    brand = models.CharField(max_length=50, verbose_name="Бренд")
    material = models.CharField(max_length=50, verbose_name="Матеріал")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна ($)")

    def __str__(self):
        return f"{self.brand} {self.name}"