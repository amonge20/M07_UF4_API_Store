from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Producto
from .serializers import ProductoSerializer  

@api_view(['GET', 'POST'])
def ver_todos_productos(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)  
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def ver_producto_detalle(request, producto_id):
    try:
        producto = Producto.objects.get(pk=producto_id)
        serializer = ProductoSerializer(producto)  
        return Response(serializer.data)
    except Producto.DoesNotExist:
        return Response({"error": "El producto no existe"}, status=404)

@api_view(['PUT'])
def actualizar_producto(request, producto_id):
    try:
        producto = Producto.objects.get(pk=producto_id)
    except Producto.DoesNotExist:
        return Response({"error": "El producto no existe"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductoSerializer(producto, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def eliminar_producto(request, producto_id):
    try:
        producto = Producto.objects.get(id=producto_id)
    except producto.DoesNotExist:
        return Response({"error": "El producto no existe"}, status=status.HTTP_404_NOT_FOUND)

    producto.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
