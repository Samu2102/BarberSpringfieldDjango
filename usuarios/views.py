from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Perfil

def login_view(request):
    if request.method == "POST":
        email    = request.POST.get('email')
        password = request.POST.get('password')

        # Buscar usuario por email
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            # Redirigir según el rol
            if user.is_superuser:
                return redirect('panel_admin')
            elif user.groups.filter(name='barberos').exists():
                return redirect('panel_barbero')
            else:
                return redirect('panel_cliente')
        else:
            messages.error(request, 'Correo o contraseña incorrectos')

    return render(request, 'login.html')


def registro_view(request):
    if request.method == "POST":
        nombre   = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        cedula   = request.POST.get('cedula')
        email    = request.POST.get('email')
        telefono = request.POST.get('telefono')
        password = request.POST.get('password')
        confirm  = request.POST.get('confirm_password')

        if password != confirm:
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, 'registro.html')

        if len(password) < 6:
            messages.error(request, 'La contraseña debe tener al menos 6 caracteres')
            return render(request, 'registro.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Ya existe una cuenta con ese correo')
            return render(request, 'registro.html')

        user = User.objects.create_user(
            username   = email,
            email      = email,
            password   = password,
            first_name = nombre,
            last_name  = apellido,
        )
        Perfil.objects.create(
    usuario=user,
    cedula=cedula,
    telefono=telefono
)
        messages.success(request, '¡Registro exitoso! Ya puedes iniciar sesión')
        return redirect('login')
    
        

    return render(request, 'registro.html')


def logout_view(request):
    logout(request)
    return redirect('inicio')