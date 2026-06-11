from django.urls import path
from . import views

urlpatterns = [
    # Barbero
    path('barbero/',            views.panel_barbero,        name='panel_barbero'),
    path('confirmar/<int:id>/', views.confirmar_cita,       name='confirmar_cita'),
    path('cancelar/<int:id>/',  views.cancelar_cita,        name='cancelar_cita'),

    # Cliente
    path('cliente/',                        views.panel_cliente,          name='panel_cliente'),
    path('cliente/agendar/',                views.agendar_cita,           name='agendar_cita'),
    path('cliente/cancelar/<int:id>/',      views.cancelar_cita_cliente,  name='cancelar_cita_cliente'),

    #inicio
    path('', views.inicio, name='inicio'),
]