from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/carrito/', include('carrito.urls')),
    path('api/catalogo/', include('catalogo.urls')),
    path('api/comandes/', include('comandes.urls')),
    path('api/pago/', include('pago.urls')),
]
