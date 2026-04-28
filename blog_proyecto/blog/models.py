from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Publicacion(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    resumen = models.CharField(max_length=200, verbose_name='Resumen')
    contenido = CKEditor5Field(verbose_name='Contenido')
    autor = models.CharField(max_length=50, verbose_name='Autor')
    imagen = models.ImageField(upload_to='publicaciones/', blank=True, null=True, verbose_name='Imagen')
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return self.titulo
