from django.shortcuts import render, redirect
from .models import Cita

# ---------- BARBERO ----------
def panel_barbero(request):
    citas = Cita.objects.all()
    return render(request, 'dashboard_barbero.html', {'citas': citas})

def confirmar_cita(request, id):
    cita = Cita.objects.get(id=id)
    cita.estado = "Confirmada"
    cita.save()
    return redirect('panel_barbero')

def cancelar_cita(request, id):
    cita = Cita.objects.get(id=id)
    cita.estado = "Cancelada"
    cita.save()
    return redirect('panel_barbero')

# ---------- CLIENTE ----------
def panel_cliente(request):
    # Por ahora el nombre del cliente está fijo; después lo sacas de request.user
    nombre_cliente = "Carlos"
    proximos = Cita.objects.filter(cliente=nombre_cliente).exclude(estado="Cancelada")
    historial = Cita.objects.filter(cliente=nombre_cliente, estado="Cancelada")
    return render(request, 'dashboard_cliente.html', {
        'nombre': nombre_cliente,
        'proximos': proximos,
        'historial': historial,
    })

def agendar_cita(request):
    if request.method == "POST":
        Cita.objects.create(
            cliente  = "Carlos",  # después: request.user.get_full_name()
            servicio = request.POST.get('servicio'),
            fecha    = request.POST.get('fecha'),
            hora     = request.POST.get('hora'),
            barbero  = request.POST.get('barbero'),
            estado   = "Pendiente",
        )
        return redirect('panel_cliente')
    return redirect('panel_cliente')

def cancelar_cita_cliente(request, id):
    cita = Cita.objects.get(id=id)
    cita.estado = "Cancelada"
    cita.save()
    return redirect('panel_cliente')

def inicio(request):
    return render(request, 'index.html')