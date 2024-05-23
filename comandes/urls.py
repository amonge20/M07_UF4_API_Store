from django.urls import path
from . import views

urlpatterns = [
    path('historial/', views.historial_comandes, name='historial_comandes'),
    path('historial/cliente/<int:cliente_id>/', views.historial_comandes_cliente, name='historial_comandes_cliente'),
    path('comandas-no-finalizadas/', views.comandas_no_finalizadas, name='comandas_no_finalizadas'),
]