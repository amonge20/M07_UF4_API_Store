from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from comandes.models import Comanda
from .models import Payment
from .serializers import PaymentSerializer
import re

def validar_tarjeta(numero_tarjeta):
    pattern = re.compile(r'^\d{16}$')
    return pattern.match(numero_tarjeta)

def validar_fecha_caducidad(fecha_caducidad):
    pattern = re.compile(r'^\d{2}/\d{2}$')
    return pattern.match(fecha_caducidad)

def validar_cvc(cvc):
    pattern = re.compile(r'^\d{3}$')
    return pattern.match(cvc)

@api_view(['POST'])
def pagar_comanda(request, comanda_id):
    try:
        comanda = Comanda.objects.get(pk=comanda_id, estado='abierta')
    except ObjectDoesNotExist:
        return Response({"estado": "error", "mensaje": "La comanda no existe o no está abierta."}, status=status.HTTP_404_NOT_FOUND)

    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid():
        datos = serializer.validated_data
        if not validar_tarjeta(datos['numero_tarjeta']):
            return Response({"estado": "error", "mensaje": "Número de tarjeta no válido."}, status=status.HTTP_400_BAD_REQUEST)
        if not validar_fecha_caducidad(datos['fecha_caducidad']):
            return Response({"estado": "error", "mensaje": "Fecha de caducidad no válida."}, status=status.HTTP_400_BAD_REQUEST)
        if not validar_cvc(datos['cvc']):
            return Response({"estado": "error", "mensaje": "CVC no válido."}, status=status.HTTP_400_BAD_REQUEST)

        Payment.objects.create(
            comanda=comanda,
            numero_tarjeta=datos['numero_tarjeta'],
            fecha_caducidad=datos['fecha_caducidad'],
            cvc=datos['cvc'],
            cantidad=datos['cantidad']
        )

        comanda.estado = 'finalizada'
        comanda.save()

        return Response({"estado": "éxito", "mensaje": "Pago realizado correctamente."}, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def consultar_estado_comanda(request, comanda_id):
    try:
        comanda = Comanda.objects.get(pk=comanda_id)
    except ObjectDoesNotExist:
        return Response({"estado": "error", "mensaje": "La comanda no existe."}, status=status.HTTP_404_NOT_FOUND)

    estado = comanda.estado
    return Response({"estado": "éxito", "mensaje": f"El estado de la comanda es {estado}."}, status=status.HTTP_200_OK)
