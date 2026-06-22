from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from citas.models import Cita
from inventario.models import Producto

@login_required(login_url='login')
def panel_barbero(request):
    citas = Cita.objects.all()
    return render(request, 'dashboard_barbero.html', {'citas': citas})

@login_required(login_url='login')
def confirmar_cita(request, id):
    cita = Cita.objects.get(id=id)
    cita.estado = "Confirmada"
    cita.save()

    return redirect('panel_barbero')

@login_required(login_url='login')
def cancelar_cita(request, id):
    cita = Cita.objects.get(id=id)

    if cita.estado != "Cancelada":

        if cita.productos and cita.productos != "Ninguno":

            productos = cita.productos.split(',')

            for nombre_producto in productos:
                nombre_producto = nombre_producto.strip()

                try:
                    producto = Producto.objects.get(nombre=nombre_producto)
                    producto.stock += 1
                    producto.save()

                except Producto.DoesNotExist:
                    pass

        cita.estado = "Cancelada"
        cita.save()

    return redirect('panel_barbero')