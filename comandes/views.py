from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comanda, Cliente
from .serializers import ComandaSerializer, ClienteSerializer
from django.shortcuts import render

@api_view(['GET'])
def historial_comandes(request):
    comandes = Comanda.objects.all()
    serializer = ComandaSerializer(comandes, many=True)
    return Response({'comandes': serializer.data})

@api_view(['GET'])
def historial_comandes_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    comandes = Comanda.objects.filter(cliente=cliente) 
    cliente_serializer = ClienteSerializer(cliente)
    comanda_serializer = ComandaSerializer(comandes, many=True)
    return Response({'cliente': cliente_serializer.data, 'comandes': comanda_serializer.data})

@api_view(['GET'])
def comandas_no_finalizadas(request):
    try:
        comandas = Comanda.objects.filter(finalizada=False)  # Filtrar comandas no finalizadas
        serializer = ComandaSerializer(comandas, many=True)
        return Response(serializer.data, status=200)
    except Exception as e:
        return Response({'message': 'Comandas no finalizadas'}, status=500)
