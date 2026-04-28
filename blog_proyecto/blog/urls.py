from django.urls import path
from .views import (
    inicio, acerca_de, lista_publicaciones,
    DetallePulicacion, crear_publicacion,
    EditarPublicacion, eliminar_publicacion, buscar
)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('about/', acerca_de, name='acerca_de'),
    path('lista/', lista_publicaciones, name='lista'),
    path('publicacion/<int:pk>/', DetallePulicacion.as_view(), name='detalle'),
    path('crear/', crear_publicacion, name='crear'),
    path('editar/<int:pk>/', EditarPublicacion.as_view(), name='editar'),
    path('eliminar/<int:pk>/', eliminar_publicacion, name='eliminar'),
    path('buscar/', buscar, name='buscar'),
]