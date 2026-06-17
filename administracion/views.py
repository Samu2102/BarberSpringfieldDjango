from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from citas.models import Cita, Barbero, Producto, Servicio

def es_admin(user):
    return user.is_superuser

@login_required(login_url='login')
@user_passes_test(es_admin, login_url='login')
def panel_admin(request):
    citas     = Cita.objects.all().order_by('-fecha')
    barberos  = Barbero.objects.all()
    productos = Producto.objects.all()
    servicios = Servicio.objects.all()
    return render(request, 'dashboard_admin.html', {
        'citas': citas,
        'barberos': barberos,
        'productos': productos,
        'servicios': servicios,
    })

@login_required(login_url='login')
@user_passes_test(es_admin, login_url='login')
def editar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    if request.method == "POST":
        cita.cliente  = request.POST.get('cliente')
        cita.servicio = request.POST.get('servicio')
        cita.fecha    = request.POST.get('fecha')
        cita.hora     = request.POST.get('hora')
        cita.barbero  = request.POST.get('barbero')
        cita.estado   = request.POST.get('estado')
        cita.save()
        messages.success(request, 'Cita actualizada correctamente')
    return redirect('panel_admin')

@login_required(login_url='login')
@user_passes_test(es_admin, login_url='login')
def agregar_barbero(request):
    if request.method == "POST":
        Barbero.objects.create(
            nombre       = request.POST.get('nombre'),
            cedula       = request.POST.get('cedula'),
            especialidad = request.POST.get('especialidad'),
            telefono     = request.POST.get('telefono'),
            email        = request.POST.get('email'),
        )
        messages.success(request, 'Barbero agregado correctamente')
    return redirect('panel_admin')

@login_required(login_url='login')
@user_passes_test(es_admin, login_url='login')
def editar_barbero(request, id):
    barbero = get_object_or_404(Barbero, id=id)
    if request.method == "POST":
        barbero.nombre       = request.POST.get('nombre')
        barbero.cedula       = request.POST.get('cedula')
        barbero.especialidad = request.POST.get('especialidad')
        barbero.telefono     = request.POST.get('telefono')
        barbero.email        = request.POST.get('email')
        barbero.save()
        messages.success(request, 'Barbero actualizado correctamente')
    return redirect('panel_admin')

@login_required(login_url='login')
@user_passes_test(es_admin, login_url='login')
def agregar_producto(request):
    if request.method == "POST":
        Producto.objects.create(
            nombre = request.POST.get('nombre'),
            precio = request.POST.get('precio'),
            stock  = request.POST.get('stock'),
        )
        messages.success(request, 'Producto agregado correctamente')
    return redirect('panel_admin')

@login_required(login_url='login')
@user_passes_test(es_admin, login_url='login')
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        producto.nombre = request.POST.get('nombre')
        producto.precio = request.POST.get('precio')
        producto.stock  = request.POST.get('stock')
        producto.save()
        messages.success(request, 'Producto actualizado correctamente')
    return redirect('panel_admin')

@login_required(login_url='login')
@user_passes_test(es_admin, login_url='login')
def agregar_servicio(request):
    if request.method == "POST":
        Servicio.objects.create(
            nombre      = request.POST.get('nombre'),
            descripcion = request.POST.get('descripcion'),
            precio      = request.POST.get('precio'),
            duracion    = request.POST.get('duracion'),
        )
        messages.success(request, 'Servicio agregado correctamente')
    return redirect('panel_admin')

@login_required(login_url='login')
@user_passes_test(es_admin, login_url='login')
def editar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    if request.method == "POST":
        servicio.nombre      = request.POST.get('nombre')
        servicio.descripcion = request.POST.get('descripcion')
        servicio.precio      = request.POST.get('precio')
        servicio.duracion    = request.POST.get('duracion')
        servicio.save()
        messages.success(request, 'Servicio actualizado correctamente')
    return redirect('panel_admin')

@login_required(login_url='login')
@user_passes_test(es_admin, login_url='login')
def eliminar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    cita.delete()
    messages.success(request, 'Cita eliminada correctamente')
    return redirect('panel_admin')

@login_required(login_url='login')
@user_passes_test(es_admin, login_url='login')
def eliminar_barbero(request, id):
    barbero = get_object_or_404(Barbero, id=id)
    barbero.delete()
    messages.success(request, 'Barbero eliminado correctamente')
    return redirect('panel_admin')

@login_required(login_url='login')
@user_passes_test(es_admin, login_url='login')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, 'Producto eliminado correctamente')
    return redirect('panel_admin')

@login_required(login_url='login')
@user_passes_test(es_admin, login_url='login')
def eliminar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    servicio.delete()
    messages.success(request, 'Servicio eliminado correctamente')
    return redirect('panel_admin')