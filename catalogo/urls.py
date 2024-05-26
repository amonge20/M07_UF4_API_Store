from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.ver_todos_productos, name='ver_todos_productos'),
    path('productos/<int:producto_id>/', views.ver_producto_detalle, name='ver_producto_detalle'),
    path('productos/update/<int:producto_id>/', views.actualizar_producto, name='actualizar_producto'),
    path('productos/delete/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]
