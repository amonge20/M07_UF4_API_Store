from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Cart
from .serializers import CartSerializer

# Create your views here.
#Creacio del "carrito"
@api_view(['POST'])
def create_cart(request):
    user = request.user
    if Cart.objects.filter(user=user, finished=False).exists():
        return Response({'message': 'Ya tienes un carrito abierto.'}, status=status.HTTP_400_BAD_REQUEST)
    cart = Cart.objects.create(user=user)
    serializer = CartSerializer(cart)
    return Response(serializer.data)