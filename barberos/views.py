from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from citas.models import Cita

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
    cita.estado = "Cancelada"
    cita.save()
    return redirect('panel_barbero')