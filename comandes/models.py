# models.py

from django.db import models

class Comanda(models.Model):
    id = models.AutoField(primary_key=True)
    total_productos = models.PositiveIntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comanda {self.id}'