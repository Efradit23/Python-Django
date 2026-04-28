from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Publicacion
from .forms import PublicacionFormulario

# Vista inicio
def inicio(request):
    return render(request, 'blog/inicio.html')

# Vista acerca de
def acerca_de(request):
    return render(request, 'blog/acerca_de.html')

# Vista lista con buscador
def lista_publicaciones(request):
    consulta = request.GET.get('consulta', '')
    if consulta:
        publicaciones = Publicacion.objects.filter(titulo__icontains=consulta)
    else:
        publicaciones = Publicacion.objects.all()
    return render(request, 'blog/lista_publicaciones.html', {
        'publicaciones': publicaciones,
        'consulta': consulta
    })

# Vista detalle
class DetallePulicacion(View):
    def get(self, request, pk):
        publicacion = get_object_or_404(Publicacion, pk=pk)
        return render(request, 'blog/detalle_publicacion.html', {'publicacion': publicacion})

# Vista crear (decorador login_required)
@login_required
def crear_publicacion(request):
    if request.method == 'POST':
        formulario = PublicacionFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista')
    else:
        formulario = PublicacionFormulario()
    return render(request, 'blog/crear_publicacion.html', {'formulario': formulario})

# Vista editar 
class EditarPublicacion(LoginRequiredMixin, View):
    def get(self, request, pk):
        publicacion = get_object_or_404(Publicacion, pk=pk)
        formulario = PublicacionFormulario(instance=publicacion)
        return render(request, 'blog/editar_publicacion.html', {'formulario': formulario})

    def post(self, request, pk):
        publicacion = get_object_or_404(Publicacion, pk=pk)
        formulario = PublicacionFormulario(request.POST, request.FILES, instance=publicacion)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista')
        return render(request, 'blog/editar_publicacion.html', {'formulario': formulario})

# Vista eliminar
@login_required
def eliminar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == 'POST':
        publicacion.delete()
        return redirect('lista')
    return render(request, 'blog/eliminar_publicacion.html', {'publicacion': publicacion})

# Vista buscar
def buscar(request):
    resultados = []
    consulta = request.GET.get('titulo', '')
    if consulta:
        resultados = Publicacion.objects.filter(titulo__icontains=consulta)
    return render(request, 'blog/buscar.html', {
        'resultados': resultados,
        'consulta': consulta
    })