from django.urls import path
from carrito import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('crearCarrito/', views.afegirCarrito, name='afegir_Carrito'),
    path('<int:cart_id>/añadirProductoCarrito/', views.afegirProducteCarrito, name='afegirProducteCarrito'),
    path('<int:cart_id>/eliminarProductoCarrito/<int:product_id>/', views.eliminarProducteCarrito, name='eliminarProducteCarrito'),
    path('<int:cart_id>/eliminarCarrito/', views.eliminarCarrito, name='eliminarCarrito'),
    path('<int:cart_id>/modificarCantidadProducto/<int:product_id>/', views.modificarCantidadProducto, name='modificarCantidadProducto'),
]