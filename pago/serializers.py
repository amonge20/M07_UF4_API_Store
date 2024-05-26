from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['numero_tarjeta', 'fecha_caducidad', 'cvc', 'cantidad']
