from django.urls import path
from . import views

urlpatterns = [
    path('pagar/<int:comanda_id>/', views.pagar_comanda, name='pagar_comanda'),
    path('estado/<int:comanda_id>/', views.consultar_estado_comanda, name='consultar_estado_comanda'),
]
