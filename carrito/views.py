from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer

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
