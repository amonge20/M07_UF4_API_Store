from django.urls import path
from . import views

urlpatterns = [
    path('crearCarrito/', views.afegirCarrito, name='afegir_Carrito'),
    path('<int:cart_id>/añadirProductoCarrito/', views.afegirProducteCarrito, name='afegirProducteCarrito'),
    path('<int:cart_id>/eliminarProductoCarrito/<int:product_id>/', views.eliminarProducteCarrito, name='eliminarProducteCarrito'),
    path('<int:cart_id>/eliminarCarrito/', views.eliminarCarrito, name='eliminarCarrito'),
    path('<int:cart_id>/modificarCantidadProducto/<int:product_id>/', views.modificarCantidadProducto, name='modificarCantidadProducto'),
    path('<int:cart_id>/listarProductos/', views.listaProductosCarrito, name='listaProductosCarrito'),
    path('<int:cart_id>/comprar/', views.comprar, name='comprar'),
]
