from django.db import models
from comandes.models import Comanda

class Payment(models.Model):
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE, related_name='pagos')
    numero_tarjeta = models.CharField(max_length=16)
    fecha_caducidad = models.CharField(max_length=5)
    cvc = models.CharField(max_length=3)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pago {self.id} para Comanda {self.comanda.id}'
