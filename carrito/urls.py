from django.urls import path
from carrito import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('createCarrito/', views.create_cart, name='create_cart'),
]