from django.urls import path
from . import views

urlpatterns = [
    path('cliente/',                   views.panel_cliente,         name='panel_cliente'),
    path('cliente/agendar/',           views.agendar_cita,          name='agendar_cita'),
    path('cliente/cancelar/<int:id>/', views.cancelar_cita_cliente, name='cancelar_cita_cliente'),
]