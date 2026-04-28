from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .models import Perfil
from .forms import FormularioRegistro, FormularioEditarUsuario, FormularioEditarPerfil

def registro(request):
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            Perfil.objects.create(usuario=usuario)
            login(request, usuario)
            messages.success(request, '¡Cuenta creada exitosamente!')
            return redirect('inicio')
    else:
        formulario = FormularioRegistro()
    return render(request, 'cuentas/registro.html', {'formulario': formulario})

def iniciar_sesion(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)
            messages.success(request, f'¡Bienvenido, {usuario.username}!')
            return redirect('inicio')
    else:
        formulario = AuthenticationForm()
    return render(request, 'cuentas/iniciar_sesion.html', {'formulario': formulario})

def cerrar_sesion(request):
    logout(request)
    messages.info(request, 'Sesión cerrada correctamente.')
    return redirect('inicio')

@login_required
def perfil(request):
    perfil, creado = Perfil.objects.get_or_create(usuario=request.user)
    return render(request, 'cuentas/perfil.html', {'perfil': perfil})

@login_required
def editar_perfil(request):
    perfil, creado = Perfil.objects.get_or_create(usuario=request.user)
    if request.method == 'POST':
        form_usuario = FormularioEditarUsuario(request.POST, instance=request.user)
        form_perfil = FormularioEditarPerfil(request.POST, request.FILES, instance=perfil)
        if form_usuario.is_valid() and form_perfil.is_valid():
            form_usuario.save()
            form_perfil.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('perfil')
    else:
        form_usuario = FormularioEditarUsuario(instance=request.user)
        form_perfil = FormularioEditarPerfil(instance=perfil)
    return render(request, 'cuentas/editar_perfil.html', {
        'form_usuario': form_usuario,
        'form_perfil': form_perfil
    })

@login_required
def cambiar_contrasena(request):
    if request.method == 'POST':
        formulario = PasswordChangeForm(request.user, request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            update_session_auth_hash(request, usuario)
            messages.success(request, 'Contraseña cambiada correctamente.')
            return redirect('perfil')
    else:
        formulario = PasswordChangeForm(request.user)
    return render(request, 'cuentas/cambiar_contrasena.html', {'formulario': formulario})