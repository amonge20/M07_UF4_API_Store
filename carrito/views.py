from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart, CartItem, Product
from .serializers import CartSerializer, AddCartItemSerializer

# Añadir Carrito
@api_view(['POST'])
def afegirCarrito(request):
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
def afegirProducteCarrito(request, cart_id):
    serializer = AddCartItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'status': 'success',
            'message': 'Producto añadido al carrito.'
        }, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Eliminar Producto del carrito
@api_view(['DELETE'])
def eliminarProducteCarrito(request, cart_id, product_id):
    try:
        cart = Cart.objects.get(id=cart_id, client=request.user, is_finalized=False)
    except Cart.DoesNotExist:
        return Response({
            'status': 'error',
            'message': 'Carrito no encontrado o ya finalizado.'
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:
        cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
    except CartItem.DoesNotExist:
        return Response({
            'status': 'error',
            'message': 'Producto no encontrado en el carrito.'
        }, status=status.HTTP_404_NOT_FOUND)
    
    cart_item.product.stock += cart_item.quantity
    cart_item.product.save()
    cart_item.delete()
    
    return Response({
        'status': 'success',
        'message': 'Producto eliminado del carrito.',
        'data': CartSerializer(cart).data
    }, status=status.HTTP_200_OK)

# Eliminar carrito
@api_view(['DELETE'])
def eliminarCarrito(request, cart_id):
    try:
        cart = Cart.objects.get(id=cart_id, client=request.user, is_finalized=False)
    except Cart.DoesNotExist:
        return Response({
            'status': 'error',
            'message': 'Carrito no encontrado o ya finalizado.'
        }, status=status.HTTP_404_NOT_FOUND)
    
    cart_items = CartItem.objects.filter(cart=cart)
    for item in cart_items:
        item.product.stock += item.quantity
        item.product.save()
        item.delete()
    
    cart.delete()
    
    return Response({
        'status': 'success',
        'message': 'Carrito eliminado completamente.'
    }, status=status.HTTP_200_OK)

# Modificar cantidad de un producto
@api_view(['PUT'])
def modificarCantidadProducto(request, cart_id, product_id):
    try:
        cart = Cart.objects.get(id=cart_id, client=request.user, is_finalized=False)
    except Cart.DoesNotExist:
        return Response({
            'status': 'error',
            'message': 'Carrito no encontrado o ya finalizado.'
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:
        cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
    except CartItem.DoesNotExist:
        return Response({
            'status': 'error',
            'message': 'Producto no encontrado en el carrito.'
        }, status=status.HTTP_404_NOT_FOUND)
    
    new_quantity = request.data.get('quantity')
    if new_quantity is None or int(new_quantity) <= 0:
        return Response({
            'status': 'error',
            'message': 'Cantidad no válida.'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    new_quantity = int(new_quantity)
    stock_difference = new_quantity - cart_item.quantity
    
    if cart_item.product.stock < stock_difference:
        return Response({
            'status': 'error',
            'message': 'Stock insuficiente para el producto solicitado.'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    cart_item.product.stock -= stock_difference
    cart_item.product.save()
    cart_item.quantity = new_quantity
    cart_item.save()
    
    return Response({
        'status': 'success',
        'message': 'Cantidad del producto actualizada.',
        'data': CartSerializer(cart).data
    }, status=status.HTTP_200_OK)

# Consultar el listado de productos del carrito
@api_view(['GET'])
def listaProductosCarrito(request, cart_id):
    try:
        cart = Cart.objects.get(id=cart_id, client=request.user, is_finalized=False)
    except Cart.DoesNotExist:
        return Response({
            'status': 'error',
            'message': 'Carrito no encontrado o ya finalizado.'
        }, status=status.HTTP_404_NOT_FOUND)
    
    cart_items = CartItem.objects.filter(cart=cart)
    serializer = AddCartItemSerializer(cart_items, many=True)
    
    return Response({
        'status': 'success',
        'message': 'Listado de productos en el carrito.',
        'data': serializer.data
    }, status=status.HTTP_200_OK)

