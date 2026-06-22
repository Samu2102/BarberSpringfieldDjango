from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from citas.models import Cita, Barbero, Servicio
from inventario.models import Producto

@login_required(login_url='login')
def panel_cliente(request):
    nombre_cliente = request.user.first_name
    proximos  = Cita.objects.filter(cliente=nombre_cliente).exclude(estado="Cancelada")
    historial = Cita.objects.filter(cliente=nombre_cliente, estado="Cancelada")
    barberos  = Barbero.objects.all()
    servicios = Servicio.objects.all()
    productos = Producto.objects.all()
    return render(request, 'dashboard_cliente.html', {
        'nombre'   : nombre_cliente,
        'proximos' : proximos,
        'historial': historial,
        'barberos' : barberos,
        'servicios': servicios,
        'productos': productos,
    })

@login_required(login_url='login')
def agendar_cita(request):
    if request.method == "POST":
        adicionales = request.POST.getlist('adicionales')
        prods_seleccionados = request.POST.getlist('productos')

        adicionales_str = ', '.join(adicionales) if adicionales else 'Ninguno'
        productos_str = ', '.join(prods_seleccionados) if prods_seleccionados else 'Ninguno'

        Cita.objects.create(
            cliente=request.user.first_name,
            servicio=request.POST.get('servicio'),
            adicionales=adicionales_str,
            productos=productos_str,
            fecha=request.POST.get('fecha'),
            hora=request.POST.get('hora'),
            barbero=request.POST.get('barbero'),
            estado="Pendiente",
        )

        # DESCONTAR INVENTARIO
        for nombre_producto in prods_seleccionados:
            try:
                producto = Producto.objects.get(nombre=nombre_producto)

                if producto.stock > 0:
                    producto.stock -= 1
                    producto.save()

            except Producto.DoesNotExist:
                pass

        return redirect('panel_cliente')

    return redirect('panel_cliente')

@login_required(login_url='login')
def cancelar_cita_cliente(request, id):
    cita = Cita.objects.get(id=id)

    # Evitar devolver inventario dos veces
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

    return redirect('panel_cliente')