from django.shortcuts import render

from django.shortcuts import render
from .models import Publicacion
from .forms import PublicacionFormulario

def inicio(request):
    return render(request, 'blog/inicio.html')

def crear_publicacion(request):
    if request.method == 'POST':
        formulario = PublicacionFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
    else:
        formulario = PublicacionFormulario()

    return render(request, 'blog/crear_publicacion.html', {'formulario': formulario})

def lista_publicaciones(request):
    consulta = request.GET.get('consulta')

    if consulta:
        publicaciones = Publicacion.objects.filter(titulo__icontains=consulta)
    else:
        publicaciones = Publicacion.objects.all()

    return render(request, 'blog/lista_publicaciones.html', {'publicaciones': publicaciones})

def buscar(request):
    resultados = []

    if request.GET.get('titulo'):
        titulo = request.GET.get('titulo')
        resultados = Publicacion.objects.filter(titulo__icontains=titulo)

    return render(request, 'blog/buscar.html', {'resultados': resultados})