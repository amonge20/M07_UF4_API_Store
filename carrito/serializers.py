from rest_framework import serializers
from .models import Carrito, ItemCarrito

class ItemCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCarrito
        fields = ['producto', 'cantidad']

class CarritoSerializer(serializers.ModelSerializer):
    items = ItemCarritoSerializer(many=True)

    class Meta:
        model = Carrito
        fields = ['usuario', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        carrito = Carrito.objects.create(**validated_data)
        for item_data in items_data:
            ItemCarrito.objects.create(carrito=carrito, **item_data)
        return carrito