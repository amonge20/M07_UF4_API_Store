from django.urls import path
from carrito import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('createCarrito/', views.create_cart, name='create_cart'),
    path('<int:cart_id>/addCarrito/', views.add_to_cart, name='add_to_cart'),
]