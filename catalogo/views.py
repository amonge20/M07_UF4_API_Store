from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Producto
from .serializers import ProductoSerializer  

@api_view(['GET'])
def ver_todos_productos(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)  
    return Response(serializer.data)


@api_view(['GET'])
def ver_producto_detalle(request, producto_id):
    try:
        producto = Producto.objects.get(pk=producto_id)
        serializer = ProductoSerializer(producto)  
        return Response(serializer.data)
    except Producto.DoesNotExist:
        return Response({"error": "El producto no existe"}, status=404)