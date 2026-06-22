from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.contrib import messages
from citas.models import Cita, Barbero, Servicio
from inventario.models import Producto
from usuarios.models import Perfil

def es_admin(user):
    return user.is_superuser

@login_required(login_url='login')
@user_passes_test(es_admin, login_url='login')
def panel_admin(request):
    citas     = Cita.objects.all().order_by('-fecha')
    barberos  = Barbero.objects.all()
    productos = Producto.objects.all()
    servicios = Servicio.objects.all()
    usuarios  = User.objects.filter(is_superuser=False).order_by('first_name')

    cantidad_barberos = User.objects.filter(
        groups__name='barberos'
    ).count()

    return render(request, 'dashboard_admin.html', {
        'citas'    : citas,
        'barberos' : barberos,
        'cantidad_barberos': cantidad_barberos,
        'productos': productos,
        'servicios': servicios,
        'usuarios' : usuarios,
    })

@login_required(login_url='login')
@user_passes_test(es_admin, login_url='login')
@login_required(login_url='login')
@user_passes_test(es_admin, login_url='login')
def asignar_barbero(request, id):
    user = get_object_or_404(User, id=id)

    grupo, _ = Group.objects.get_or_create(name='barberos')
    user.groups.add(grupo)

    # Buscar el perfil real del usuario
    perfil = Perfil.objects.filter(usuario=user).first()

    if not perfil:
        messages.error(
            request,
            f'{user.first_name} no tiene perfil registrado.'
        )
        return redirect('panel_admin')

    # Crear registro de barbero si no existe
    if not Barbero.objects.filter(email=user.email).exists():
        Barbero.objects.create(
            nombre=f"{user.first_name} {user.last_name}",
            cedula=perfil.cedula,
            telefono=perfil.telefono,
            especialidad="General",
            email=user.email,
        )

    messages.success(
        request,
        f'{user.first_name} ahora tiene rol de barbero'
    )

    return redirect('panel_admin')

@login_required(login_url='login')
@user_passes_test(es_admin, login_url='login')
def quitar_barbero(request, id):
    user = get_object_or_404(User, id=id)

    grupo, _ = Group.objects.get_or_create(name='barberos')
    user.groups.remove(grupo)

    Barbero.objects.filter(email=user.email).delete()

    user.save()

    messages.success(
        request,
        f'{user.first_name} ya no es barbero'
    )

    return redirect('panel_admin')

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