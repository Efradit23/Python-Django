from django.urls import path
from .views import inicio, crear_publicacion, lista_publicaciones, buscar

urlpatterns = [
    path('', inicio),
    path('crear/', crear_publicacion),
    path('lista/', lista_publicaciones),
    path('buscar/', buscar),
]