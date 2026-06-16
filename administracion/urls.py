from django.urls import path
from . import views

urlpatterns = [
    path('admin-panel/',                       views.panel_admin,      name='panel_admin'),
    path('admin-panel/editar-cita/<int:id>/',  views.editar_cita,      name='editar_cita'),
    path('admin-panel/agregar-barbero/',       views.agregar_barbero,  name='agregar_barbero'),
    path('admin-panel/editar-barbero/<int:id>/', views.editar_barbero, name='editar_barbero'),
    path('admin-panel/agregar-producto/',      views.agregar_producto, name='agregar_producto'),
    path('admin-panel/editar-producto/<int:id>/', views.editar_producto, name='editar_producto'),
    path('admin-panel/agregar-servicio/',      views.agregar_servicio, name='agregar_servicio'),
    path('admin-panel/editar-servicio/<int:id>/', views.editar_servicio, name='editar_servicio'),
]