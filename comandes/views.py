# comandes/views.py
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comanda
from .serializers import ComandaSerializer

@api_view(['GET'])
def historial_comandes(request):
    comandes = Comanda.objects.all()
    serializer = ComandaSerializer(comandes, many=True)
    return Response({'comandes': serializer.data})
