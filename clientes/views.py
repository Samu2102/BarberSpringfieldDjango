from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from citas.models import Cita

@login_required(login_url='login')
def panel_cliente(request):
    nombre_cliente = request.user.first_name
    proximos = Cita.objects.filter(cliente=nombre_cliente).exclude(estado="Cancelada")
    historial = Cita.objects.filter(cliente=nombre_cliente, estado="Cancelada")
    return render(request, 'dashboard_cliente.html', {
        'nombre': nombre_cliente,
        'proximos': proximos,
        'historial': historial,
    })

@login_required(login_url='login')
def agendar_cita(request):
    if request.method == "POST":
        Cita.objects.create(
            cliente  = request.user.first_name,
            servicio = request.POST.get('servicio'),
            fecha    = request.POST.get('fecha'),
            hora     = request.POST.get('hora'),
            barbero  = request.POST.get('barbero'),
            estado   = "Pendiente",
        )
        return redirect('panel_cliente')
    return redirect('panel_cliente')

@login_required(login_url='login')
def cancelar_cita_cliente(request, id):
    cita = Cita.objects.get(id=id)
    cita.estado = "Cancelada"
    cita.save()
    return redirect('panel_cliente')