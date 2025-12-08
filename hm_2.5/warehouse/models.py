from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    min_players = models.IntegerField()
    max_players = models.IntegerField()
    genre = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.price} UAH)"