from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comanda, Cliente
from .serializers import ComandaSerializer, ClienteSerializer

@api_view(['GET'])
def historial_comandes(request):
    comandes = Comanda.objects.all()
    serializer = ComandaSerializer(comandes, many=True)
    return Response({'comandes': serializer.data})

@api_view(['GET'])
def historial_comandes_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    serializer = ClienteSerializer(cliente)
    return Response({'cliente': serializer.data})