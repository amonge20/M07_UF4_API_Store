from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart, CartItem, Product
from .serializers import CartSerializer, AddCartItemSerializer

# Añadir Carrito
@api_view(['POST'])
def create_cart(request):
    client = None
    if request.user.is_authenticated:
        client = request.user
    cart = Cart(client=client)
    cart.save()
    
    serializer = CartSerializer(cart)
    return Response({
        'status': 'success',
        'message': 'Carrito creado correctamente.',
        'data': serializer.data
    }, status=status.HTTP_201_CREATED)

# Añadir Producto al Carrito
@api_view(['POST'])
def add_to_cart(request, cart_id):
    serializer = AddCartItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'status': 'success',
            'message': 'Producto añadido al carrito.'
        }, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)