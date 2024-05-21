from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.ver_todos_productos, name='ver_todos_productos'),
    path('productos/<int:producto_id>/', views.ver_producto_detalle, name='ver_producto_detalle'),
]