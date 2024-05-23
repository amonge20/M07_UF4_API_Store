# comandes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('historial/', views.historial_comandes, name='historial_comandes'),
    path('historial/cliente/<int:cliente_id>/', views.historial_comandes_cliente, name='historial_comandes_cliente'),
]