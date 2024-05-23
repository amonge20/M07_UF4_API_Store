# comandes/serializers.py
from rest_framework import serializers
from .models import Comanda, Cliente

class ComandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comanda
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    comandes = ComandaSerializer(many=True, read_only=True)

    class Meta:
        model = Cliente
        fields = '__all__'