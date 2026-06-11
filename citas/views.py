from django.shortcuts import render, redirect
from .models import Cita

def panel_barbero(request):

    citas = Cita.objects.all()

    return render(
        request,
        'dashboard_barbero.html',
        {
            'citas': citas
        }
    )

def confirmar_cita(request, id):

    cita = Cita.objects.get(id=id)

    cita.estado = "Confirmada"

    cita.save()

    return redirect('/')

def cancelar_cita(request, id):

    cita = Cita.objects.get(id=id)

    cita.estado = "Cancelada"

    cita.save()

    return redirect('/')