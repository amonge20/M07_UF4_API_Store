from rest_framework import serializers
from .models import Cart, CartItem, Product, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'

class AddCartItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def validate(self, data):
        product_id = data.get('product_id')
        quantity = data.get('quantity')

        if not product_id:
            raise serializers.ValidationError('El ID del producto es requerido.')
        
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise serializers.ValidationError('El producto especificado no existe.')

        if not quantity:
            raise serializers.ValidationError('La cantidad es requerida.')

        if product.stock < quantity:
            raise serializers.ValidationError('No hay suficiente stock para este producto.')

        return data

    def create(self, validated_data):
        product = Product.objects.get(pk=validated_data['product_id'])
        cart = self.context['cart']
        return CartItem.objects.create(
            cart=cart,
            product=product,
            quantity=validated_data['quantity']
        )

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
